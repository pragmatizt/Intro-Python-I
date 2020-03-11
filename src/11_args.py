"""11 can be applied for 14"""
# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

def f1(arg1, arg2):
    return arg1 + arg2 

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"
"""GREAT RESOURCE: https://www.geeksforgeeks.org/args-kwargs-python/ """
"""Another GREAT TUTOR: http://pythontutor.com/visualize.html#mode=edit"""

def f2(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

    #     sum = sum + float(arg)
    # print("Number of arguments are:", len(argv))
    # return sum

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
"""Is it really as simple as changing the "for i in args" to for i in a"?
So the "call function" is the "for i in a" here, and not "return sum"?"""
def f2(*argv):
    sum = 0
    for i in a:
        sum += i
    return sum

print(f2(a))    # Should print 22


# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

"""GREAT RESOURCE: https://www.programiz.com/python-programming/function-argument 
Function arguments can have default values in Python. We can provide a default value 
to an argument by using the assignment operator (=)."""

# def f3():

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(d)
