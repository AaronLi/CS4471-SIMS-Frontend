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
    backend_response = stub.ReadItem(item_messages.ReadItemRequest(user_id="usertest",shelf_id="shelf1"))
    print(backend_response)


if __name__ == '__main__':
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    channel = grpc.insecure_channel('localhost:50052')
    # frontend_grpc.add_SimsFrontendServicer_to_server(FrontendServicer(), server)
    stub = backend_grpc.SimsInventoryInformationSystemStub(channel)
    testGetItem(stub)
    # server.add_insecure_port('[::]:50051')
    # server.start()
    # print("Running")
    # server.wait_for_termination()