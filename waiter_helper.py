# Waiter helper program

# Create a menu for the restaurant
menu = ["macaroni cheese", "chilli", "fish and chips", "arancini", "nachos", "garlic bread"]

# Display menu
print("Menu:")
for item in menu:
    print(item)

# Let the customer order three times
order_no = 0
order_items = []
while order_no < 3:
    new_item = input("Please enter an order item ")
    order_items.append(new_item)
    order_no += 1
