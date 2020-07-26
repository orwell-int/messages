env/bin/activate:
	virtualenv env
	. env/bin/activate && pip install -r requirements.txt

develop: env/bin/activate

test: env/bin/activate
	. env/bin/activate && ./test.sh
