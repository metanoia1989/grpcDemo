#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from concurrent import futures
import logging

import grpc
import os
import logging
from proto import hello_pb2, hello_pb2_grpc


class Gretter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f'hello, {request.name}!')

    def SayHelloAgain(self, request, context):
        return hello_pb2.HelloReply(message=f'hello agian, {request.name}')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    hello_pb2_grpc.add_GreeterServicer_to_server(Gretter(), server)
    server.add_insecure_port('[::]:50051')
    logging.info('server have been starting and listening localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
