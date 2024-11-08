# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["Apple", "Banana", "Guava", "Pear", "Orange", "Strawberry", "Kiwi"]
# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)
print("Done with the fruit task!")
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Done with the countdown task!")
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for n in range (1, 11):
    square = n **2
    print(square)
print("Done with the square task!")
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
list_colors = ("Red", "Pink", "Yellow", "Blue", "Green", "Black", "Brown")
# TODO: Use a for loop to select and print 3 random colors from the list
for colour in range(3):
   colour = random.choice(list_colors)
   print(colour)
print("Done with the colors task!")
#-------------------------
# ------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations
print(math_operations.add(1, 2))
print(math_operations.subtract(4, 3))
print(math_operations.multiply(5, 6))
print(math_operations.divide(7, 8))
print("Done with the custom module task!")

# TODO: Use a while loop to create a simple calculator
import math_operations

def calculator():
    print("calculator")
    print("Available operations: +, -, *, /")
    print("Type 'exit' to quit calculator")

    while True:
        operation = input("Enter a Math Operation(+, -, *, /): ")

        if operation.lower() == "exit":
            print("Thank You For Using The Calculator. We'll Calculate Next Time!")
            break

        try:
            num1 = int(input("Enter the first value: "))
            num2 = int(input("Enter the second value: "))

        except ValueError:
            print("Invalid Value. Please Insert Numerical Values")

        if operation == "+":
            result = math_operations.add(num1, num2)
            print(result)

        elif operation == "-":
            result = math_operations.subtract(num1, num2)
            print(result)

        elif operation == "*":
            result = math_operations.multiply(num1, num2)
            print(result)

        elif operation == "/":
            result = math_operations.divide(num1, num2)
            print(result)

        else:
            print("Unkown operation. Please check and try again")

calculator()

    