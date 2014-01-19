clean_pb()
{
	cd "$(dirname "$0")"
	grep "_pb2\.py" .gitignore | xargs rm
}

clean_pb
