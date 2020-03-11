"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

print("=====FOO TEXT=====")
foo = open('foo.txt', 'r')
print(foo.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

"""Create new document"""
bar = open('bar.txt', 'w+')

"""Write three lines in new document"""
print("\r\n=====BAR TEXT=====")
bar.write('Ah you think darkness is your ally? \nYou merely adopted the dark. I was born in it, molded by it. \nI didn\'t see the light until I was already a man, by then it was nothing to me but blinding!')

"""Close the text to save changes"""
bar.close()

"""Now let's inspect it:"""
bar = open('bar.txt', 'r')
print(bar.read())
bar.close()