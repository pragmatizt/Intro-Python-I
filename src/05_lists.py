# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

"""this is a good link for some list methods: https://lucidar.me/en/python/insert-append-extend-concatanate-lists/"""

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.insert(3, 4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
"""It becomes a list within a list, so that's not right"""
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
"""Removing element from lists: https://note.nkmk.me/en/python-list-clear-pop-remove-del/"""
x.pop(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
"""Inserting elements in python lists: https://developers.google.com/edu/python/lists"""
x.insert(5,99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
"""multiplying elements in a list by a number: https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number/35166717"""
"""Does this solution count?"""
product = []
for i in x:
    product.append(i*1000)
print(product)

# Asked someone else how they did it, this was their code:
print([i * 1000 for i in x])