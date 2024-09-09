# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # Create a list of student names
    students = ['Femi', 'Emre', 'Greg']
    
    # Assign the second student's name to first_student
    first_student = students[1]
    
    # Assign the last student's name to last_student
    last_student = students[-1]
    
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # Create a tuple of foods
    foods = ('salmon', 'steak', 'pizza')
    
    # Initialize an empty string
    meal = ''
    
    # Use a loop to concatenate each food item to the meal string
    for food in foods:
        meal += food + ' '
    
    return meal.strip()  # Remove trailing space

# Call the function and print the result
print('Exercise 2:', combine_foods())


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # Create a tuple of foods
    foods = ('jollof', 'chopcheese', 'pancakes')
    
    # Slice the tuple to get the last two food strings
    last_two = foods[-2:]
    
    return last_two

# Call the function and print the result
print('Exercise 3:', slice_foods())


# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    # Create a dictionary with city, state, and population
    home_town = {
        'city': 'Queens',
        'state': 'New York',
        'population': 89405
    }
    
    # Format a string using the dictionary
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())


# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # Define the home_town dictionary
    home_town = {
        'city': 'Atlanta',
        'state': 'Georgia',
        'population': 681204
    }
    
   
    home_town_items = []
    
    # Iterate over the dictionary items
    for key, value in home_town.items():
        # Append formatted string to the list
        home_town_items.append(f"{key} = {value}")
    
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())
