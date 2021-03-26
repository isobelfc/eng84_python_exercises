# empty list that we will add items into
xmas_list = []

# ask the user to input their list
making_list = True
while making_list:  # loop will continue while making_list is true
    new_item = input("What would you like for Christmas? ")
    if "exit" in new_item:
        making_list = False  # ends loop
    else:
        xmas_list.append(new_item)  # add new item to list

# print the created list
print("Christmas List:")
for item in xmas_list:  # iterates over each item in list
    print(f"{xmas_list.index(item) + 1} - {item}")
# xmas_list.index(item) returns the position of the item in the list
# we add 1 because python indexing starts from 0, but we want our numbers to start from 1
