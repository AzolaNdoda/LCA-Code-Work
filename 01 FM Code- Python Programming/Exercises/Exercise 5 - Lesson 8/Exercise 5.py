# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["Banana", "Strawberry", "Kiwi", "Pear"]
# TODO: Add a fruit to the end of the list
fruits.append("Guava")
print(fruits)

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"Watermelon")
print(fruits)
# TODO: Remove a fruit from the list
fruits.remove("Banana")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]
print(numbers)
# TODO: Create a new list with each number squared
numbers_squared = [1*1, 2*2, 3*3, 4*4, 5*5]
print(numbers_squared)
# TODO: Find the sum and average of the original numbers
average = sum(numbers) / len(numbers)
# TODO: Print the results
print(average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
Countries_capitals= {
    "Belgium": "Brussels",
    "China": "Beijing",
    "Cuba": "Havana",
    "Greece": "Athens",
    "Italy": "Rome"}

# TODO: Add a new country-capital pair
Countries_capitals.update({"SA": "Pretoria"})
print(Countries_capitals)
# TODO: Update the capital of an existing country
Countries_capitals.update({"Italy": "Paris"})
print(Countries_capitals)

# TODO: Remove a country-capital pair
Countries_capitals.pop("Belgium")
# TODO: Print the modified dictionary
print(Countries_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "Banana": "Yellow",
    "Strawberry": "Red",
    "Apple": "Green"}
# TODO: Print all the fruits (keys)

keys = fruit_colors.keys()
print(keys)
# TODO: Print all the colors (values)
values = fruit_colors.values()
print(values)
# TODO: Print each fruit and its color
 
for keys,values in fruit_colors.items():
    print(f"{keys} : {values}")

# TODO: Check if a fruit is in the dictionary and print its color
print(fruit_colors.get("Strawberry"))