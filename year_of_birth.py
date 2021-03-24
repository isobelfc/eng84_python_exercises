# Calculate year of birth

# # First simple version - no input checks, not accounting for birthday
# # Define variables age and name
# name = input("Please enter your name ")
# age = int(input("How old are you? "))  # input returns a string, so cast to integer
# birth_year = (2021 - age)
#
# print(f"OMG, {name}, you are {age} years old, so you were born in {birth_year}")


# # Second version - check if birthday has happened yet this year, check age is number
# # Define name variable
# name = input("Please enter your name ")
#
# # Check age is a number
# age_input = True
# while age_input:
#     age = input("How old are you? ")
#     if age.isdigit():  # checks that age is a digit
#         age_input = False
#     else:
#         print("Please enter your age in digits")
#
# # Make sure that this question is answered with either Y or N with a while loop
# birthday_input = True
# while birthday_input:
#     birthday = input("Have you already had your birthday this year? Y/N ")
#     if birthday == "Y":
#         birthday_input = False
#     elif birthday == "N":
#         birthday_input = False
#     else:
#         print("Please answer Y or N")
#
# # Calculate birth year with birthday accounted for
# if birthday == "Y":
#     birth_year = (2021 - int(age))
# elif birthday == "N":
#     birth_year = (2021 - int(age) - 1)
# else:
#     print("Something went wrong")
#
# print(f"OMG, {name}, you are {age} years old, so you were born in {birth_year}")


# Third version - get current year from datetime library
# Get current year
from datetime import datetime  # datetime library contains many date and time functions
current_datetime = datetime.now()  # datetime.now() returns full date and time
current_year = int(current_datetime.strftime("%Y"))  # returns only the year from full date and time
# strftime() returns year as a string, so cast it to integer
# print(current_year)  # check year is returned correctly

# Define name variable
name = input("Please enter your name ")

# Check age is a number
age_input = True
while age_input:
    age = input("How old are you? ")
    if age.isdigit():  # checks that age is a digit
        age_input = False
    else:
        print("Please enter your age in digits")

# Make sure that this question is answered with either Y or N with a while loop
birthday_input = True
while birthday_input:
    birthday = input("Have you already had your birthday this year? Y/N ")
    if birthday == "Y":
        birthday_input = False
    elif birthday == "N":
        birthday_input = False
    else:
        print("Please answer Y or N")

# Calculate birth year with birthday accounted for
# Replaced hardcoded year with current year calculated above
if birthday == "Y":
    birth_year = (current_year - int(age))
elif birthday == "N":
    birth_year = (current_year - int(age) - 1)
else:
    print("Something went wrong")

# Print user's name, age, and birth year
print(f"OMG, {name}, you are {age} years old, so you were born in {birth_year}")
