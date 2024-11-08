#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
def check_attendance(students, absentees):
    return absentees

# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.
students = ["Alice", "Bob", "Charlie", "David"]
absentees = ["Bob", "David"]
for absentees in check_attendance(students, absentees):
    print([absentees])

#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.
def calculate_average_grade(student_names, student_grades):
    return average_grade
# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.
calculate_average_grade = {
    "Alice": 85,
     "Bob": 92,
     "Charlie": 78,
     "David": 90}

values = calculate_average_grade.values()
average_grade = sum(values) / len(values)
print(average_grade)
#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.
def operation_selector(math_operation):
    if math_operation == "add":
        return lambda a,b: a+b
    elif math_operation == "multiply":
        return lambda a,b: a*b
    else:
        return("Invalid opperation")
  
# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
add_operation = operation_selector("add")
a = 4
b = 6
result = a + b
print(result)

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
a= 3
b = 7
multiply_operation = operation_selector("multiply")
result = a * b
print(result)
#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    fuel_needed = distance / fuel_efficiency
    total_fuel_price = fuel_needed * fuel_price
    return total_fuel_price


# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)


# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# TODO: Use a for loop to print each item and its quantity in stock.

for items in grocery_inventory.items():
    print(f"{items}")

# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).
values = grocery_inventory.values()
print(sum(values))

#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# TODO: Ask the user to input their PIN.
# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

correct_pin = "1234"
attempts = 0
while attempts < 3:
    user_pin = input("Please input your PIN: ")

    if user_pin == correct_pin:
        print("Access Granted")
        break

    attempts += 1
    print("Incorrect pin.Try again")

    if attempts == 3:
        print("Account Locked")


# TODO: Use a while loop to implement the retry system.
while attempts < 3:
    user_pin = input("Please input your PIN: ")

    if user_pin == correct_pin:
        print("Access Granted")
        break

    attempts += 1
    print("Incorrect pin.Try again")

    if attempts == 3:
        print("Account Locked")

#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).
# TODO: Use a for loop to calculate the total score.
# TODO: Calculate and print the average score for the class.
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.
import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Use a for loop to calculate the total score.
total_score = 0
for score in scores:
    total_score += score

# TODO: Calculate and print the average score for the class.
average_score = total_score / len(scores)

print(f"Scores: {scores}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")

# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.
if average_score > 75:
    print("Congratulations and Well done!")

import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]
print(scores)

# TODO: Calculate total and average scores.


#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.
# TODO: Print the names of the selected team members.

import random

# List of participants.
participants = ["Person1", "Person2", "Person3", ..., "Person20"]
participants = ["Azola", "Alulutho", "Sbahle", "Moesha", "Asanda", "Kyle", "Alice", "Sam"]
# TODO: Randomly select 5 people from the participants list.
random_people = random.sample(participants, 5)
for person in random_people:
    print(person)

#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
# TODO: Ask the user to input the distance they walked, ran, and cycled today.
# TODO: Calculate and print the total calories burned for each activity.
# TODO: Sum and print the total calories burned for the day.
import fitness_tracker

walk_distance = float(input("Please insert the distance you walked: "))
run_distance = float(input("Please insert the distance you ran: "))
cycle_distance = float(input("Please input the distance you cycled: "))

walk_calories = fitness_tracker.walk_calories(walk_distance)
run_calories = fitness_tracker.run_calories(run_distance)
cycle_calories = fitness_tracker.cycle_calories(cycle_distance)

print(f"Calories burned  while walking: {walk_calories} km")
print(f"Calories burned while running: {run_calories} km")
print(f"Calories burned while cycling: {cycle_calories} km")

total_calories = walk_calories + run_calories + cycle_calories
print(f"The total calories burned for the day: {total_calories} km")


#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.
# TODO: Ask the user to input their monthly repayment amount.
# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
# TODO: Print the remaining loan amount after each payment.
# TODO: When the loan is fully paid off, print a congratulatory message.
loan_amount = float(input("Please input the total loan amount: "))
repayment_amount = float(input("Please input your monthly repayment amount: "))

month = 1
while loan_amount > 0:
    
    loan_amount -= repayment_amount

    if loan_amount < 0:
        loan_amount = 0
    print(f"Month {month}: Remaining loan amount is R{loan_amount:.2f}")
    month += 1


#loan_amount = float(input("Enter the total loan amount: "))
#monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate the repayment process.
month = 1
while loan_amount > 0:
    
    loan_amount -= repayment_amount

    if loan_amount < 0:
        loan_amount = 0
    print(f"Month {month}: Remaining loan amount is R{loan_amount:.2f}")
    month += 1
