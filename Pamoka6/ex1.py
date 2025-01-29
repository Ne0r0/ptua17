# Write a Python program that asks the user to enter their name, surname, and age. 
# Store these values in a dictionary with keys 'name', 'surname', and 'age'. 
# Print the dictionary.

# Example output:
# {'name': 'John', 'surname': 'Doe', 'age': 30}

user_name = str(input("Write your name: "))
user_surname = str(input("Write your surname: "))
user_age = int(input("Write your age: "))

my_dict = {"name" : user_name, "surname" : user_surname, "age" : user_age}
print(my_dict)