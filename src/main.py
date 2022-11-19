from proto.frontend.frontend_pb2_grpc import SimsFrontendServicer

class FrontendServicer(SimsFrontendServicer):

    def CredAuth(self, request, context):
        return super().CredAuth(request, context)

    def ClientCmd(self, request, context):
        return super().ClientCmd(request, context)


if __name__ == '__main__':
    print("Hello, World!")