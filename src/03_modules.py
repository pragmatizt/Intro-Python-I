"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

"""sys.argv is a list in Python, which contains the command-line arguments passed to the script."""

# Print out the command line arguments in sys.argv, one per line:
for items in sys.argv:
    print(items)

# Print out the OS platform you're using:
print("OS platform used:",sys.platform)

"""Original answer: sys.getwindowsversion
sys.getwindowsversion(major=10, minor=0, build=18363, platform=2, service_pack='')"""

# Print out the version of Python you're using:
print("Version of Python used:",sys.version)

"""Original answer: sys.version_info.
sys.getwindowsversion(major=10, minor=0, build=18363, platform=2, service_pack='')"""

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# print("OS platform used is:", d))

# Print the current process ID
print("Current process:", os.getpid())


# Print the current working directory (cwd):
print("Current working directory is:", os.getcwd())

# Print out your machine's login name
print("Current machine's login name:", os.getlogin())