from concurrent import futures
from typing import List

import frontend_proto.frontend_pb2_grpc as frontend_grpc
import frontend_proto.frontend_messages_pb2 as frontend_messages
import backend_proto.iis_pb2_grpc as backend_grpc
import backend_proto.item_messages_pb2 as item_messages
import backend_proto.shelf_messages_pb2 as shelf_messages
import backend_proto.slot_messages_pb2 as slot_messages
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

    def CreateShelf(self, request, context):
        print("Rquest {} {}".format(request.username, request.token))
        try:
            self.authenticate_user(request.username, request.token)
            return frontend_messages.ActionApproved()
        except sqlite3.Error as e:
            print("Can't connect to db, error %s" % e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Can't fetch from db")


    def GetShelves(self, request, context):
        print("Rquest {} {}".format(request.username, request.token))
        try:
            self.authenticate_user(request.username, request.token)
            backend_shelves: List[shelf_messages.ShelfInfo] = stub.ReadShelf(shelf_messages.ReadShelfRequest(user_id=request.username)).info
            response = [frontend_messages.ShelfInfo(shelf_id=shelf.shelf_id, shelf_count=shelf.shelf_count) for shelf in backend_shelves]
            return frontend_messages.Shelves(response)
        except sqlite3.Error as e:
            print("Can't connect to db, error %s" % e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Can't fetch from db")

    def GetItems(self, request, context):
        print("Rquest {} {}".format(request.username, request.token))
        try:
            self.authenticate_user(request.username, request.token)
            backend_items: List[item_messages.ItemInfo] = stub.ReadItem(item_messages.ReadItemRequest(user_id=request.username,shelf_id=request.shelf_id)).info
            response = [frontend_messages.ItemInfo(description=item.description, object_id=item.object_id, shelf_id=item.shelf_id, price=item.price, stock=item.stock) for item in backend_items]
            return frontend_messages.Items(items=response)
        except sqlite3.Error as e:
            print("Can't connect to db, error %s" % e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Can't fetch from db")

    def authenticate_user(self, username, token):
        connect = CredentialDB()
        cur = connect.cur.execute("""SELECT token, tokenTime FROM credential WHERE username = ?""",
                                  ((username,)))
        if cur:
            tokenInfo = cur.fetchone()
            dbToken = tokenInfo[0]
            dbTokenTimestamp = tokenInfo[1]
            tokenLife = time.time() - dbTokenTimestamp
            if dbToken == token and tokenLife > 2628000:
                raise Exception("Token expired")
        else:
            raise Exception("Auth database not available")

    def _shelvesMessageGenerator(self, shelf=None):
        dummyShelf = {
            "dummy1": frontend_messages.ShelfInfo(shelf_id='dummy1',shelf_count=1),
            "dummy2": frontend_messages.ShelfInfo(shelf_id='dummy2',shelf_count=2),
            "dummy3": frontend_messages.ShelfInfo(shelf_id='dummy3',shelf_count=3),
            "dummy4": frontend_messages.ShelfInfo(shelf_id='dummy4',shelf_count=4)
        }   
        if shelf == "":
            return dummyShelf.values()
        else:
            if shelf in dummyShelf:
                return [dummyShelf.get(shelf)]
            else:
                raise Exception("No such shelf")   

    def _itemsMessageGenerator(self, shelf=None):
        dummyItem = {
            "dummy1": frontend_messages.ItemInfo(description='dummy1', object_id='dummy1',price=1, stock=1),
            "dummy2": frontend_messages.ItemInfo(description='dummy2',  object_id='dummy2',price=2, stock=2),
            "dummy3": frontend_messages.ItemInfo(description='dummy3', object_id='dummy3',price=3, stock=3),
            "dummy4": frontend_messages.ItemInfo(description='dummy4', object_id='dummy4',price=4, stock=4)
        }
        if shelf == "":   
            return dummyItem.values()
        else:
            if shelf in dummyItem:
                return dummyItem.get(shelf)
            else:
                raise Exception("No such shelf")    
    
    def _listReadGeneratort(self,type):
        pass


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    channel = grpc.insecure_channel('localhost:50052')
    frontend_grpc.add_SimsFrontendServicer_to_server(FrontendServicer(), server)
    stub = backend_grpc.SimsInventoryInformationSystemStub(channel)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Running")
    server.wait_for_termination()
