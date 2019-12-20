import optparse
import os
import platform
import shutil
import subprocess
import sys
import tarfile
import tempfile


# Get abspath of current python file
print(os.path.abspath(__file__))


# Get dir of current python file
print(os.path.dirname(os.path.abspath(__file__)))


# Get abspath under a dir 
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'packages')
print(path)

# join a path
path = os.path.join('~', '.local', 'lib', 'aws')
print(path)


# get abs path of current user
path =  os.path.expanduser(os.path.join('~', '.local', 'lib', 'aws'))
print(path)

print(os.environ['HOME'])
print(os.path.expandvars('$HOME'))
print(os.path.expanduser('~'))

# get currend dir like pwd
original = os.getcwd()
# change dir like cd 
os.chdir(dirname)