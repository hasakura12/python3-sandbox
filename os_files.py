import sys
import os
from dotenv import load_dotenv 
import helpers

from pathlib import Path

def print_python_ver():
    helpers.display("Python version=" + str(sys.version) + ", version info=" + str(sys.version_info))

def read_env():
    load_dotenv()
    username = os.getenv("USERNAME")
    print(f"Username={username}")

# ref: https://www.youtube.com/watch?v=JgT3jIh05po&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=12
def file_operations():
    cwd = Path.cwd()
    print(f"cwd={cwd}")

    new_file = Path.joinpath(Path.cwd(), "test.txt")
    print(f"{new_file} exists? {new_file.exists()}")

    print(f"Is {cwd} directory? {cwd.is_dir()}")
    print(f"Is {cwd} file? {cwd.is_file()}")

def read():
    file = "tests/test.txt"

    # file mode: https://youtu.be/QDYIMoA9EOg?t=83
    # r=read, a=append, w=write, +=update
    try:
        stream = open(file, "r") # open file as read mode
    
        print(f"Is {file} readable? {stream.readable()}")
        print(f"First char in {file} is '{stream.read(1)}'")
        print(f"First line in {file} is '{stream.readline()}'")
    finally:
        stream.close()

def write():
    file = "tests/test.txt"

    # with open() as stream will close() at the end of block
    with open(file, "a+") as stream: # append file

        print(f"Is {file} writabe? {stream.writable()}")
        stream.writelines(["Writing from Python\n"])

        # move cursor to beginning
        stream.seek(0)
        print(f"Updated {file} content is '{stream.read()}'")


print()
print("~WORKING ON PYTHON VER...")
print_python_ver()


print()
print("~WORKING ON ENV...")
read_env()

print()
print("~WORKING ON FILES...")
file_operations()

print()
print("~WORKING ON READING FILES...")
read()

print()
print("~WORKING ON WRITING FILES...")
write()
