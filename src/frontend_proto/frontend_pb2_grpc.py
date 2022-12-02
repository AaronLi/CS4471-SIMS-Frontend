# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from frontend_proto import frontend_messages_pb2 as frontend__proto_dot_frontend__messages__pb2


class SimsFrontendStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CredAuth = channel.unary_unary(
                '/sims_ims_frontend.SimsFrontend/CredAuth',
                request_serializer=frontend__proto_dot_frontend__messages__pb2.LoginRequest.SerializeToString,
                response_deserializer=frontend__proto_dot_frontend__messages__pb2.Token.FromString,
                )
        self.SignUp = channel.unary_unary(
                '/sims_ims_frontend.SimsFrontend/SignUp',
                request_serializer=frontend__proto_dot_frontend__messages__pb2.LoginRequest.SerializeToString,
                response_deserializer=frontend__proto_dot_frontend__messages__pb2.ActionApproved.FromString,
                )
        self.ClientCmd = channel.unary_unary(
                '/sims_ims_frontend.SimsFrontend/ClientCmd',
                request_serializer=frontend__proto_dot_frontend__messages__pb2.ClientAction.SerializeToString,
                response_deserializer=frontend__proto_dot_frontend__messages__pb2.ActionApproved.FromString,
                )
        self.GetShelves = channel.unary_unary(
                '/sims_ims_frontend.SimsFrontend/GetShelves',
                request_serializer=frontend__proto_dot_frontend__messages__pb2.GetShelvesRequest.SerializeToString,
                response_deserializer=frontend__proto_dot_frontend__messages__pb2.Shelves.FromString,
                )


class SimsFrontendServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CredAuth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignUp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientCmd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShelves(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimsFrontendServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CredAuth': grpc.unary_unary_rpc_method_handler(
                    servicer.CredAuth,
                    request_deserializer=frontend__proto_dot_frontend__messages__pb2.LoginRequest.FromString,
                    response_serializer=frontend__proto_dot_frontend__messages__pb2.Token.SerializeToString,
            ),
            'SignUp': grpc.unary_unary_rpc_method_handler(
                    servicer.SignUp,
                    request_deserializer=frontend__proto_dot_frontend__messages__pb2.LoginRequest.FromString,
                    response_serializer=frontend__proto_dot_frontend__messages__pb2.ActionApproved.SerializeToString,
            ),
            'ClientCmd': grpc.unary_unary_rpc_method_handler(
                    servicer.ClientCmd,
                    request_deserializer=frontend__proto_dot_frontend__messages__pb2.ClientAction.FromString,
                    response_serializer=frontend__proto_dot_frontend__messages__pb2.ActionApproved.SerializeToString,
            ),
            'GetShelves': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShelves,
                    request_deserializer=frontend__proto_dot_frontend__messages__pb2.GetShelvesRequest.FromString,
                    response_serializer=frontend__proto_dot_frontend__messages__pb2.Shelves.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sims_ims_frontend.SimsFrontend', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimsFrontend(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CredAuth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sims_ims_frontend.SimsFrontend/CredAuth',
            frontend__proto_dot_frontend__messages__pb2.LoginRequest.SerializeToString,
            frontend__proto_dot_frontend__messages__pb2.Token.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignUp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sims_ims_frontend.SimsFrontend/SignUp',
            frontend__proto_dot_frontend__messages__pb2.LoginRequest.SerializeToString,
            frontend__proto_dot_frontend__messages__pb2.ActionApproved.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientCmd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sims_ims_frontend.SimsFrontend/ClientCmd',
            frontend__proto_dot_frontend__messages__pb2.ClientAction.SerializeToString,
            frontend__proto_dot_frontend__messages__pb2.ActionApproved.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShelves(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sims_ims_frontend.SimsFrontend/GetShelves',
            frontend__proto_dot_frontend__messages__pb2.GetShelvesRequest.SerializeToString,
            frontend__proto_dot_frontend__messages__pb2.Shelves.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
