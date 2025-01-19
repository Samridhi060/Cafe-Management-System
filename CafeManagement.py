# Author : Samridhi Gupta
# Date : 20/01/2025
# Project : Cafe Management System

def ordered_items():
    for item_name, (quantity, price) in order_items.items():
        total_price = price * quantity
        print(f"{item_name} X {quantity} = {total_price}")

# Function to recalculate the total order
def calculate_total():
    total = 0
    for item_name, (quantity, price) in order_items.items():
        total += price * quantity
    return total

def delete_item_from_order(item_to_delete, plates_to_delete):
    """Delete a specified number of plates of an item from the order if it exists."""
    for key in list(order_items.keys()):
        if key.lower() == item_to_delete.lower():  # Case-insensitive match
            current_quantity, price = order_items[key]
            if plates_to_delete >= current_quantity:
                del order_items[key]
                print(f"All plates of {key} have been removed from your order.")
            else:
                order_items[key][0] -= plates_to_delete
                print(f"{plates_to_delete} plates of {key} have been removed from your order.")
            return
    print(f"{item_to_delete} is not in your order.")

menu = {
    1: ('Pizza', 200),
    2: ('Pasta', 350),
    3: ('Burger', 200),
    4: ('Sandwich', 150),
    5: ('Cold Coffee', 100),
    6: ('Hot Coffee', 50),
    7: ('Cold Drink', 50),
    8: ('Salad', 300)
}

print("Welcome to the Love Cafe")
print("---Menu---")
for item, (name, price) in menu.items():
    print(f"{item}. {name}: {price}")

order_items = {}
another_order = 'y'

while another_order == 'y':
    try:
        order = int(input("What would you like to order? (Enter the item number): "))
        if order in menu:
            item_name, item_price = menu[order]
            plates = int(input("Enter the number of plates: "))
            
            # Update order_items dictionary with quantity and price
            if item_name in order_items:
                order_items[item_name][0] += plates  # Update quantity
            else:
                order_items[item_name] = [plates, item_price]  # Store quantity and price
            
            print(f"You have ordered {item_name} X {plates} plates.")
        else:
            print("Ordered item is not available yet.")
    except ValueError:
        print("Please enter a valid integer corresponding to the menu item.")

    another_order = input("Would you like to order another item? (y/n): ").lower()

# Display the ordered items
print(f"Your Ordered items are:")
ordered_items()

# Display total before deletion
order_total = calculate_total()
print(f"Your total order is: {order_total}")

# Ask the user if they want to delete any item
while order_items:
    delete_item = input("Would you like to delete an item from your order? (y/n): ").lower()
    
    if delete_item != 'y':
        break
    
    item_to_delete = input("Please enter the name of the item you want to delete: ").strip()
    
    # Ask how many plates to delete
    plates_to_delete = int(input(f"How many plates of {item_to_delete} would you like to delete? "))
    
    delete_item_from_order(item_to_delete, plates_to_delete)
    
    # Recalculate the total after deletion
    order_total = calculate_total()
    
    # Display the updated order summary
    print(f"Updated Ordered items are:")
    ordered_items()
    print(f"Your total order is: {order_total}")

# Final order summary
print("Final order summary:")
ordered_items()
print(f"Your final total is: {order_total}")
