# write a program that input order from user and order again,
# then calculate items.


menu = {
    "Burger":200,
    "Pasta":350,
    "Coffee":150,
    "Fries":200,
    "Water bottle":100,
    "Cold drink":120
}

# Say welcome to customer:

print("Welcome to our Restaurant")

# Display menu:

print("Burger: Rs 200\nPasta: Rs 350\nCoffee: Rs 150\nFries: Rs 200\nWater bottle: Rs 100\nCold drink: Rs 120")

order_total = 0

# Enter first item:

item_1 = input("Enter the item you want to order")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added")
else:
    print(f"This item {item_1} is not Avaliable")
    
# Enter another item: 
 
another_order = input("Do you want to add another order? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the another item")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your order {item_2} has been added")
    else:
         print(f"This item {item_2} is not Avaliable")

# Total Amount:

print(f"The total amount of items to pay: {order_total}")