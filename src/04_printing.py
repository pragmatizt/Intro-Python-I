"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is", x, ", y is", '%.2f' % y, ", z is", '"'+z+'"')

"""Interesting, so I'll need to read more about what the + signs 
in front of and behind z do."""

# Use the 'format' string method to print the same thing
print('x is', x, ', y is', "{0:.2f}".format(y), ', z is', '"'+z+'"')

"""So is the biggest value add of the format string the curly braces 
and the .format()?"""

# Finally, print the same thing using an f-string
print('x is {}, y is {}, z is "{}"'.format(x, "{0:.2f}".format(y), z))

"""I definitely like this the best -- makes the most intuitive sense, too!"""
