print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# NOTE: We put a end=' ' at the end of each print line. 
# This tells print to not end the line with a newline character 
# and go to the next line.
 
# Python input() Function:
# Example: Ask for the user's name and print it:

# print('Enter your name:')
# x = input()
# print('Hello, ' + x)

# Example: Use the prompt parameter to write a message before the input:
# x = input('Enter your name:')
# print('Hello, ' + x)