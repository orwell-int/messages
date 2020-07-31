do_test()
{
	cd "$(dirname "$0")"
	./generate.sh
	PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}$PWD python orwell/messages/test/test_messages.py
}

do_test
