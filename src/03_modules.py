"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
import fileinput
for line in fileinput.input():
    process(line)

# Print out the OS platform you're using:
print(sys.getwindowsversion())

"""When I run on terminal, this is the output.  Not sure if this is right.
sys.getwindowsversion(major=10, minor=0, build=18363, platform=2, service_pack='')"""

# Print out the version of Python you're using:
print(sys.version_info)

"""Also not sure if this is right."""

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

# Print the current working directory (cwd):
# YOUR CODE HERE

# Print out your machine's login name
# YOUR CODE HERE
