clean_pb()
{
	dir="$(dirname "$(readlink -e "$0")")"
	cd $dir
	grep "_pb2\.py" .gitignore | xargs rm
}

clean_pb
