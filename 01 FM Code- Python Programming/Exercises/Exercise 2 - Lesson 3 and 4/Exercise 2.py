# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 0
x = x + 3

# TODO: Multiply y by 2 using the *= operator
y = 2
y = y * 2

# TODO: Divide x by y and store the result in a variable called 'result'
result = x/y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 20
b = 16
if a > b: 
    print("a is greater than b")
  
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b = 16
if b %2 == 0:
    print("even")
else:
    print("odd")

# TODO: Create a condition that checks if c is less than or equal to a
a = 20
c = 5
if c <= a:
    print("c is less than or equal to a")
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = True
if (a > b) or (b %2) and (c <= a):
    print(final_condition)
else:
    print("False")
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("what is your test score? " ))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score in range (90,101):
    print("A")
elif score in range (80,90):
    print("B")
elif score in range (70,80):
    print("C")
elif score in range (60,70):
    print("D")
else:
    print("F")
# TODO: Print the grade for the given score
print("score:",score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("what is the value of num1? "))
num2 = int(input("what is the value of num2? "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("what operation will you use(+, -, *, /)? ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "/" and num2 == 0:
    result = num1/num2
    print("Invalid")
elif operation == "+":
    results = num1+num2
elif operation == "-":
    results = num1-num2
elif operation == "*":
    results = num1*num2
elif operation == "/":
    results = num1/num2

# TODO: Handle the case of division by zero


# TODO: Print the result of the operation
print(results)