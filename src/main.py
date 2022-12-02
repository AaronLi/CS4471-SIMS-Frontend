from concurrent import futures

import frontend_proto.frontend_pb2_grpc as frontend_grpc
import frontend_proto.frontend_messages_pb2 as frontend_messages
import grpc
import time
import sqlite3
import logging
import secrets
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import bcrypt, bcrypt_check
from authdb import CredentialDB

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class FrontendServicer(frontend_grpc.SimsFrontendServicer):
    def SignUp(self, request, context):
        print("Signup",request.username, request.password)
        b64pwd = b64encode(SHA256.new(request.password.encode('utf-8')).digest())
        bcrypt_hash = bcrypt(b64pwd,12)
        try:
            connect = CredentialDB()
            cur = connect.cur.execute("""INSERT INTO credential VALUES (?, ?, NULL, NULL)""",(request.username,memoryview(bcrypt_hash)))
            connect.conn.commit()
            return frontend_messages.ActionApproved()
        except sqlite3.Error as e:
            print("Can't connect to db, error %s" % e)
            error_string = str(e)
            if "UNIQUE constraint" in error_string and "credential.username" in error_string:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details("Username exists")
                return frontend_grpc.Response()
            else:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details("Can't fetch from db")
                return frontend_grpc.Response()
    
    def CredAuth(self, request, context):
        print("CredAuth", type(request.username), request.password)

        try:
            connect = CredentialDB()
            cur = connect.cur.execute("""SELECT hashedPw FROM credential WHERE username = ?""",((request.username,)))
            if cur: hashedPw = cur.fetchone()[0]
            else:
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details('User not found!')
                return frontend_grpc.Response()
            inputPwB = request.password.encode('utf-8')
            try:
                b64input = b64encode(SHA256.new(inputPwB).digest())
                bcrypt_check(b64input, hashedPw)
                token = secrets.token_urlsafe(16)
                tokenTime = time.time()
                connect.cur.execute("""UPDATE credential SET token = :token,  tokenTime = :tokenTime WHERE username = :username""",{"token":token, "tokenTime":tokenTime, "username":request.username})
                connect.conn.commit()
                return frontend_messages.Token(token=token)
            
            except ValueError:
                print("Incorrect passworßd")
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details('Incorrect password!')
                return frontend_grpc.Response()
            
        except sqlite3.Error as e:
            print("Can't connect to db, error %s" % e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Can't fetch from db")
            return frontend_grpc.Response()

        # return frontend_messages.Token(token="placeholder")

    def ClientCmd(self, request, context):


        return super().ClientCmd(request, context)

    def GetShelves(self, request, context):
        print("Rquest {} {}".format(request.username, request.token))
        try:
            connect = CredentialDB()
            cur = connect.cur.execute("""SELECT token, tokenTime FROM credential WHERE username = ?""",
                                      ((request.username,)))
            if cur:
                dbToken = cur.fetchone()[0]
                dbTokenTimestamp = cur.fetchone()[1]
                tokenLife = time.time() - dbTokenTimestamp
                if dbToken == request.token and tokenLife < 300:
                    return frontend_messages.Shelves(self._messageGenerator)
                else:
                    raise Exception("Token expired")
        except sqlite3.Error as e:
            print("Can't connect to db, error %s" % e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Can't fetch from db")

    def _messageGenerator(self):
        dummyShelf = [
            frontend_messages.ShelfInfo(shelf_id='dummy1',shelf_count=1),
            frontend_messages.ShelfInfo(shelf_id='dummy2',shelf_count=2),
            frontend_messages.ShelfInfo(shelf_id='dummy3',shelf_count=3),
            frontend_messages.ShelfInfo(shelf_id='dummy4',shelf_count=4)
        ]   
        return dummyShelf


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    frontend_grpc.add_SimsFrontendServicer_to_server(FrontendServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Running")
    server.wait_for_termination()
