do_test()
{
	dir="$(dirname "$(readlink -e "$0")")"
	cd "$dir"
	./generate.sh
	PYTHONPATH=$PYTHONPATH:$(pwd) python orwell/messages/test/test_messages.py
}

do_test
