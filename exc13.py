from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
print("The sciprt is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Run from CLI / Command prompt:
#
# $ python3.6 ex13.py first 2nd 3rd
#
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd
#
# You can actually replace first, 2nd, and 3rd with any three things you want.
#