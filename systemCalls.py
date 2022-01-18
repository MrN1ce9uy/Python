#! /usr/bin/python3

import os
from subprocess import call

print("CWD: ",os.getcwd())
print("UID: ",os.getuid())
print("ENV: ",os.getenv("PATH"))

os.system("ls -la")

inp = input("Hit enter")
call(["ls", "-la"])
