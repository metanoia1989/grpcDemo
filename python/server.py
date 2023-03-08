#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

from .proto import haberdasher_pb2, haberdasher_twirp

class HaberdasherService(object):
    def MakeHat(self, context, size):
        if size.inches <= 0:
            raise InvalidArgument(argument="inches", error="I can't make a hat that small!")
        return haberdasher_pb2.Hat(
            size=size.inches,
            color= random.choice(["white", "black", "brown", "red", "blue"]),
            name=random.choice(["bowler", "baseball cap", "top hat", "derby"])
        )

# if you are using a custom prefix, then pass it as `server_path_prefix`
# param to `HaberdasherServer` class.
service = haberdasher_twirp.HaberdasherServer(service=HaberdasherService())
app = TwirpASGIApp()
app.add_service(service)
