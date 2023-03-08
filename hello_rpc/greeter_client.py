#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import grpc
from proto import hello_pb2, hello_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        res = stub.SayHello(hello_pb2.HelloRequest(name='you'))
        print('res' + res.message)

        res = stub.SayHelloAgain(hello_pb2.HelloRequest(name='you'))
        print('res again' + res.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
