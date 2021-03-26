# Waiter helper program

# Create a menu for the restaurant
menu = ["macaroni cheese", "chilli", "fish and chips", "arancini", "nachos", "garlic bread", "falafels"]

# Display menu
print("Menu:")
for item in menu:
    print(item)  # prints each item in the menu

# Let the customer order three times
ordering = True
order_items = []
while ordering:
    new_item = input("Please enter an order item, or enter 'x' to finish ")
    if new_item in menu:
        order_items.append(new_item)  # only add the item to the order if it is on the menu
        print("Thank you, noted")  # confirmation message when correctly entered
    elif new_item == "x":
        ordering = False  # ordering set to False will end the loop
    else:
        print("Please make sure the item is on the menu, or enter 'x' to finish")

# Read back order in formatted way
print("You have ordered:")
for item in order_items:
    print(item)
