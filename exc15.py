# importing argv from sys-moddule:
from fileinput import close
from sys import argv

# defines/equals the variable argv to script and filename:
script, filename = argv

# Variable txt performs the command open that opens 
# the filename defined at the prompt (CLI) to begin with: 
txt = open(filename)

# Formatted print-string displaying the filename defined 
# at the prompt/CLI:
print(f"Here's your file {filename}:")
# Prints the contents of the prompt-defined txt-file by .read'ing it:
print(txt.read())

# prompts for input (=The filename) from the user and uses the
# user-input as a variable (=file_again):
print("Type the filenmae again:")
file_again = input("> ")

# defines the variable txt_again by open'ing the above defined
# variable (=file_again):
txt_again = open(file_again)

# Prints the contents of the above input (the file to be opened
# = file_again by using the .read-command)
print(txt_again.read())

# Closing the above opened file(s) - does it work(?):
txt.close()
txt_again.close()

# exc15_sample.txt is a part of this script when opening the script 
# with python from the CLI