do_generate()
{
	dir="$(dirname "$(readlink -e "$0")")"
	cd "$dir"
	protoc -I=. --python_out=orwell/messages controller.proto robot.proto server-game.proto server-web.proto version1.proto
}

do_generate
