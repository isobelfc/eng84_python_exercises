# # make a loop with a range that says hello 10 times
# for num in range(10):  # range(10) starts at 0 and stops at 9 (before 10)
#     print("Hello")

# Create another loop with a range that asks for names and appends to list names
names = []
for num in range(10):
    new_name = input("Please enter a name ")
    names.append(new_name)

# # check names are appended
# print(names)

# Make a loop that iterates over each name in lit_name and formats it into lowercase in a new variable called list names lower
list_names_lower = []
for name in names:
    list_names_lower.append(name.lower())

# print lower case name list
print(list_names_lower)

# Iterate over a list of values to find if they are even
