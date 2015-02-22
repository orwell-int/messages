#!/bin/sh
do_generate()
{
	cd "$(dirname "$0")"
	protoc -I=. --python_out=orwell/messages controller.proto robot.proto server-game.proto server-web.proto
}

do_generate
