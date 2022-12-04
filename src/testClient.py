from concurrent import futures

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

def testGetItem(stub):
    backend_response = stub.ReadItem(item_messages.ReadItemRequest(user_id="usertest",item_id=1223))
    print(backend_response)

def testGetShelf(stub):
    backend_response = stub.ReadShelf(shelf_messages.ReadShelfRequest(user_id="usertest"))
    print(backend_response)

def testInsertShelf(stub):
    info = shelf_messages.ShelfInfo(shelf_id="shelf2",shelf_count=10)
    backend_response = stub.CreateShelf(shelf_messages.CreateShelfRequest(user_id="usertest",info=info))
    print(backend_response)

def testInsertItem(stub):
    info = item_messages.ItemInfo(description="testing item",object_id=7777,shelf_id="shelf1",price=10.55,stock=15)
    backend_response = stub.CreateItem(item_messages.CreateItemRequest(user_id="usertest",info=info))
    print(backend_response)



if __name__ == '__main__':
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    channel = grpc.insecure_channel('localhost:50052')
    # frontend_grpc.add_SimsFrontendServicer_to_server(FrontendServicer(), server)
    stub = backend_grpc.SimsInventoryInformationSystemStub(channel)
    # testGetItem(stub)
    testInsertItem(stub)
    # testInsertShelf(stub)
    # server.add_insecure_port('[::]:50051')
    # server.start()
    # print("Running")
    # server.wait_for_termination()