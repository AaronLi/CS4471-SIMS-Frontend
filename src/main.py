from concurrent import futures

import frontend_proto.frontend_pb2_grpc as frontend_grpc
import frontend_proto.frontend_messages_pb2 as frontend_messages
import grpc
class FrontendServicer(frontend_grpc.SimsFrontendServicer):
    def CredAuth(self, request, context):
        print("CredAuth", request.username, request.password)
        return frontend_messages.Token(token="placeholder")

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
