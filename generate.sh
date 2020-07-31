#!/bin/sh
do_generate()
{
	cd "$(dirname "$0")"
	protoc --version
	protoc -I=. --python_out=orwell/messages common.proto controller.proto robot.proto server-game.proto server-web.proto
	sed "/^import common_pb2 as common__pb2$/s//from . import common_pb2 as common__pb2/" -i orwell/messages/*_pb2.py
	sed "/^from common_pb2 import \*$/s//from .common_pb2 import */" -i orwell/messages/*_pb2.py
}

do_generate
