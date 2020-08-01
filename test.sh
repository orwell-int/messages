do_test()
{
	cd "$(dirname "$0")"
	python3 generate.py
	PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}$PWD python3 orwell/messages/test/test_messages.py
}

do_test
