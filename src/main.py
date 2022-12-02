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
                return frontend_messages.Token(token=token)
            
            except ValueError:
                print("Incorrect password")
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
        print("ClientCmd")
        return super().ClientCmd(request, context)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    frontend_grpc.add_SimsFrontendServicer_to_server(FrontendServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Running")
    server.wait_for_termination()
