import os
import sys
import subprocess
import glob

import tempfile
import shutil

from inspect import currentframe, getframeinfo
from pathlib import Path


def replace(file_path, replacements):
    fh, abs_path = tempfile.mkstemp()
    with os.fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                for old, new in replacements:
                    if old in line:
                        line = line.replace(old, new)
                new_file.write(line)
    os.remove(file_path)
    shutil.move(abs_path, file_path)


def main():
    filename = getframeinfo(currentframe()).filename
    parent = Path(filename).resolve().parent

    os.chdir(parent)
    if len(sys.argv) > 1:
        destination = sys.argv[1]
    else:
        destination = "."
    destination = Path(destination).resolve()
    target = os.path.join(destination, "orwell", "messages")
    if not os.path.exists(target):
        os.makedirs(target)
    init = os.path.join(target, "__init__.py")
    if not os.path.exists(init):
        with open(init, "w"):
            # create empty file
            pass
    proto_files = glob.glob("*.proto")
    command = ["protoc", "--version"]
    print("run", command)
    subprocess.run(command)
    command = ["protoc", "--python_out", target] + proto_files
    print("run", command)
    subprocess.run(command)
    # need to patch generated files as they can not be imported
    os.chdir(target)
    generated_files = glob.glob("*_pb2.py")
    print("generated files:", generated_files)
    for file in generated_files:
        replace(
            file,
            [("import common_pb2 as common__pb2",
              "from . import common_pb2 as common__pb2"),
             ("from common_pb2 import *",
              "from .common_pb2 import *")])


if "__main__" == __name__:
    main()
