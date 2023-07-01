import json

menu = {}
orders = {}

def display_menu():
    print("Zesty Zomato Menu:")
    print("------------------")
    print("Dish ID\t\tDish Name\t\tPrice\t\tAvailability")
    print("------------------------------------------------")

    for dish_id, dish in menu.items():
        print(f"{dish_id}\t\t{dish['name']}\t\t${dish['price']}\t\t{'Yes' if dish['availability'] else 'No'}")

def add_dish():
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available? (yes/no): ").lower() == 'yes'

    menu[dish_id] = {
        'name': dish_name,
        'price': price,
        'availability': availability
    }
    print(f"{dish_name} has been added to the menu.")

def remove_dish():
    dish_id = input("Enter the dish ID to remove: ")
    if dish_id in menu:
        dish_name = menu[dish_id]['name']
        del menu[dish_id]
        print(f"{dish_name} has been removed from the menu.")
    else:
        print("Invalid dish ID.")

def update_dish_availability():
    dish_id = input("Enter the dish ID to update availability: ")
    if dish_id in menu:
        availability = input("Is the dish available? (yes/no): ").lower() == 'yes'
        menu[dish_id]['availability'] = availability
        print("Dish availability updated.")
    else:
        print("Invalid dish ID.")

def take_order():
    customer_name = input("Enter customer name: ")
    order_ids = input("Enter dish IDs separated by commas: ").split(',')
    order_status = 'received'
    total_price = 0.0
    
    for order_id in order_ids:
        if order_id not in menu:
            print(f"Dish with ID {order_id} does not exist.")
            return
        elif not menu[order_id]['availability']:
            print(f"Dish {menu[order_id]['name']} is not available.")
            return
        else:
            total_price += menu[order_id]['price']
    
    order_id = str(len(orders) + 1)
    order = {
        'customer_name': customer_name,
        'order_ids': order_ids,
        'status': order_status,
        'total_price': total_price
    }
    orders[order_id] = order
    
    print(f"Order ID: {order_id}")
    print(f"Customer: {customer_name}")
    print("Order Details:")
    for order_id in order_ids:
        print(f"- {menu[order_id]['name']}")
    print(f"Total Price: ${total_price:.2f}")
    print("Status: Received")



def update_order_status():
    order_id = input("Enter the order ID to update status: ")
    if order_id in orders:
        status = input("Enter the new status: ")
        orders[order_id]['status'] = status
        print("Order status updated.")
    else:
        print("Invalid order ID.")

def review_orders():
    print("Zesty Zomato Orders:")
    print("--------------------")
    for order_id, order in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Customer: {order['customer_name']}")
        print("Order Details:")
        for order_id in order['order_ids']:
            print(f"- {menu[order_id]['name']}")
        print(f"Total Price: ${order['total_price']:.2f}")
        print(f"Status: {order['status']}")
        print("------------")

def filter_orders_by_status():
    status = input("Enter the order status to filter: ")
    filtered_orders = [order for order in orders.values() if order['status'] == status]
    if len(filtered_orders) > 0:
        print(f"Orders with status '{status}':")
        print("--------------------")
        for order in filtered_orders:
            print(f"Order ID: {order_id}")
            print(f"Customer: {order['customer_name']}")
            print("Order Details:")
            for order_id in order['order_ids']:
                print(f"- {menu[order_id]['name']}")
            print(f"Total Price: ${order['total_price']:.2f}")
            print(f"Status: {order['status']}")
            print("------------")
    else:
        print(f"No orders with status '{status}' found.")

def save_data():
    with open("/menu.json", "w") as menu_file:
        json.dump(menu, menu_file, indent=4)
    with open("/orders.json", "w") as orders_file:
        json.dump(orders, orders_file, indent=4)

# Load menu and orders data from files
try:
    with open("/menu.json", "r") as menu_file:
        menu = json.load(menu_file)
except FileNotFoundError:
    menu = {}

try:
    with open("/orders.json", "r") as orders_file:
        orders = json.load(orders_file)
except FileNotFoundError:
    orders = {}

# Main loop
while True:
    print("\nZesty Zomato - Main Menu")
    print("------------------------")
    print("1. Display Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Update Dish Availability")
    print("5. Take Order")
    print("6. Update Order Status")
    print("7. Review Orders")
    print("8. Filter Orders by Status")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        display_menu()
    elif choice == '2':
        add_dish()
    elif choice == '3':
        remove_dish()
    elif choice == '4':
        update_dish_availability()
    elif choice == '5':
        take_order()
    elif choice == '6':
        update_order_status()
    elif choice == '7':
        review_orders()
    elif choice == '8':
        filter_orders_by_status()
    elif choice == '9':
        save_data()
        break
    else:
        print("Invalid choice. Please try again.")




























































# # Define the initial menu
# menu = {}

# def display_menu():
#     print("Zesty Zomato Menu:")
#     print("------------------")
#     print("Dish ID\t\tDish Name\t\tPrice\t\tAvailability")
#     print("------------------------------------------------")

#     for dish_id, dish in menu.items():
#         print(f"{dish_id}\t\t{dish['name']}\t\t${dish['price']}\t\t{'Yes' if dish['availability'] else 'No'}")

# def add_dish():
#     dish_id = input("Enter the dish ID: ")
#     dish_name = input("Enter the dish name: ")
#     price = float(input("Enter the price: "))
#     availability = input("Is the dish available? (yes/no): ").lower() == 'yes'

#     menu[dish_id] = {
#         'name': dish_name,
#         'price': price,
#         'availability': availability
#     }
#     print(f"{dish_name} has been added to the menu.")

# def remove_dish():
#     dish_id = input("Enter the dish ID to remove: ")
#     if dish_id in menu:
#         dish_name = menu[dish_id]['name']
#         del menu[dish_id]
#         print(f"{dish_name} has been removed from the menu.")
#     else:
#         print("Invalid dish ID.")

# def update_dish_availability():
#     dish_id = input("Enter the dish ID to update availability: ")
#     if dish_id in menu:
#         availability = input("Is the dish available? (yes/no): ").lower() == 'yes'
#         menu[dish_id]['availability'] = availability
#         print("Dish availability updated.")
#     else:
#         print("Invalid dish ID.")

# # def take_order():
# #     customer_name = input("Enter customer name: ")
# #     order_ids = input("Enter dish IDs separated by commas: ").split(',')
# #     order_status = 'received'
# #     # Check if dishes exist and are available
# #     for order_id in order_ids:
# #         if order_id not in menu:
# #             print(f"Dish with ID {order_id} does not exist.")
# #             return
# #         elif not menu[order_id]['availability']:
# #             print(f"Dish {menu[order_id]['name']} is not available.")
# #             return
# #     # Process the order
# #     order_id = str(len(menu) + 1)
# #     order = {
# #         'customer_name': customer_name,
# #         'order_ids': order_ids,
# #         'status': order_status
# #     }
# #     print(f"Order ID: {order_id}")
# #     print(f"Customer: {customer_name}")
# #     print("Order Details:")
# #     for order_id in order_ids:
# #         print(f"- {menu[order_id]['name']}")
# #     print("Status: Received")


# def take_order():
#     customer_name = input("Enter customer name: ")
#     order_ids = input("Enter dish IDs separated by commas: ").split(',')
#     order_status = 'received'
#     total_price = 0.0
    
#     for order_id in order_ids:
#         if order_id not in menu:
#             print(f"Dish with ID {order_id} does not exist.")
#             return
#         elif not menu[order_id]['availability']:
#             print(f"Dish {menu[order_id]['name']} is not available.")
#             return
#         else:
#             total_price += menu[order_id]['price']
    
#     order_id = str(len(orders) + 1)
#     order = {
#         'customer_name': customer_name,
#         'order_ids': order_ids,
#         'status': order_status,
#         'total_price': total_price
#     }
#     orders[order_id] = order
    
#     print(f"Order ID: {order_id}")
#     print(f"Customer: {customer_name}")
#     print("Order Details:")
#     for order_id in order_ids:
#         print(f"- {menu[order_id]['name']}")
#     print(f"Total Price: ${total_price:.2f}")
#     print("Status: Received")


# def update_order_status():
#     order_id = input("Enter the order ID to update status: ")
#     if order_id in orders:
#         status = input("Enter the new status: ")
#         orders[order_id]['status'] = status
#         print("Order status updated.")
#     else:
#         print("Invalid order ID.")

# def review_orders():
#     print("All Orders:")
#     print("------------")
#     for order_id, order in orders.items():
#         print(f"Order ID: {order_id}")
#         print(f"Customer: {order['customer_name']}")
#         print("Order Details:")
#         for order_id in order['order_ids']:
#             print(f"- {menu[order_id]['name']}")
#         print(f"Status: {order['status']}")
#         print("------------")


# def filter_orders_by_status():
#     status = input("Enter the order status to filter: ")
#     filtered_orders = [order for order in orders.values() if order['status'] == status]
#     if len(filtered_orders) > 0:
#         print(f"Orders with status '{status}':")
#         print("--------------------")
#         for order in filtered_orders:
#             print(f"Order ID: {order_id}")
#             print(f"Customer: {order['customer_name']}")
#             print("Order Details:")
#             for order_id in order['order_ids']:
#                 print(f"- {menu[order_id]['name']}")
#             print(f"Total Price: ${order['total_price']:.2f}")
#             print(f"Status: {order['status']}")
#             print("------------")
#     else:
#         print(f"No orders with status '{status}' found.")


# import json

# # Load menu and orders data from a file
# try:
#     with open("/menu.json", "r") as menu_file:
#         menu = json.load(menu_file)
# except FileNotFoundError:
#     menu = {}

# try:
#     with open("/orders.json", "r") as orders_file:
#         orders = json.load(orders_file)
# except FileNotFoundError:
#     orders = {}

# # Save menu and orders data to a file
# def save_data():
#     with open("/menu.json", "w") as menu_file:
#         json.dump(menu, menu_file, indent=4)
#     with open("/orders.json", "w") as orders_file:
#         json.dump(orders, orders_file, indent=4)




# # # Main loop
# # while True:
# #     print("\nZesty Zomato - Main Menu")
# #     print("------------------------")
# #     print("1. Display Menu")
# #     print("2. Add Dish")
# #     print("3. Remove Dish")
# #     print("4. Update Dish Availability")
# #     print("5. Take Order")
# #     print("6. Update Order Status")
# #     print("7. Review Orders")
# #     print("8. Exit")

# #     choice = input("Enter your choice (1-8): ")

# #     if choice == '1':
# #         display_menu()
# #     elif choice == '2':
# #         add_dish()
# #     elif choice == '3':
# #         remove_dish()
# #     elif choice == '4':
# #         update_dish_availability()
# #     elif choice == '5':
# #         take_order()
# #     elif choice == '6':
# #         update_order_status()
# #     elif choice == '7':
# #         review_orders()
# #     elif choice == '8':
# #         break
# #     else:
# #         print("Invalid choice. Please try again.")
