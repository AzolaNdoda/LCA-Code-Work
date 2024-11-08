# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("what is your name? ")
# TODO: Ask the user for their age and store it in a variable
age = input("what is your age? ")
# TODO: Print a greeting using the name and age variables
print("Hello "+ name + " " + age)
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("what is the length of the rectangle? "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("what is the width of the rectangle? "))
# TODO: Calculate the area of the rectangle
area = length * width
# TODO: Print the result
print(area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temperature_C = float(input("what is the temperature in Celsius? "))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
temperature_F = round((temperature_C * 9/5 )+ 32, 2)
# TODO: Print the result rounded to two decimal places
print(temperature_F)