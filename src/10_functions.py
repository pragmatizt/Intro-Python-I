# Write a function is_even that will return true if the passed-in number is even.
"""Here's a great resource: https://www.tes.com/blog/creating-a-function-odd-or-even"""

# Ask during 1:1 why below didn't work. Below gave "Odd!"
def is_even(n):
    return n % 2 == 0
# def is_even(num):
#     if (num % 2) == 0:
#         return True
#     else:
#         return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

print("Even!" if is_even(num) is True else 'Odd!')

