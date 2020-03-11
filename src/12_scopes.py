# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12  # Global

def change_x():
    global x  # Designating "global x"
    x = 99  # Local

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
"""We have to designate "global x" within the function"""
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y  # Designating "nonlocal y"
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)

"""This was a great resource to help me with this module: 
https://www.programiz.com/python-programming/global-local-nonlocal-variables"

outer()
