# fra modulet sys importeres argv, som tager imod argumenter/filer
# udenfor python
# "sys.argv is a list in Python, which contains the command-line 
# arguments passed to the script.":

from sys import argv

# Defines the variables associated with argv:
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# input("?") = Prompts for contiuening by pressing RETURN
# or cancelling the program (CTRL-C):
input("?")

# Defines the variable 'target' to be opening the above defined
# file. 'w' enables the script to Write into the file:
print("Opening the file...")
target = open(filename, 'w')

# target.truncate() erases the contents of the file:
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# Defines the variables Line1-3 by the input from the user:
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

# Writes the input above into the above defined file (originally
# defined at the command prompt/CLI: python exc16.py exc16_test.txt):
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# A shorter way to do the above writing to the txt-file:
lines=(line1, line2, line3)
target.write('\n'.join(lines))
target.write('\n')

print("And finally, we close it.")
target.close()