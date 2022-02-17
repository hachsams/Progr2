# Defines a variable:
types_of_people = 10
# Defines a variable containing a f-string (format-string):
x = f"There are {types_of_people} types of people."

# Equals the variables to text-strings:
binary = "binary"
do_not = "don't"
# Defines a variable containing a f-string (format-string):
y = f"Those who know {binary} and those who {do_not}."

# Prints the predefined variables x and y:
print(x)
print(y)

# Prints the predefines variables x and y (also containing f-strings) inside f-strings:
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Sets variable to be a boolean value (true/false):
hilarious = False
# Sets the variable to be a text-string containing curly brackets, open to further inputs:
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints the variable above using the .format()-syntax which also prints the boolean value of the hilarious variable:
print(joke_evaluation.format(hilarious))

# Sets the variables to be text-strings:
w = "This is the left side of..."
e = "a string with a right side."

# Prints both variables containing the text-strings above:
print(w + e)