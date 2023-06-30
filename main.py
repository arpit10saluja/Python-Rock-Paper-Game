class Snack:
    def __init__(self, snack_id, snack_name, price, availability):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.availability = availability



class SnackInventory:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack):
        self.inventory.append(snack)
        print(f"Snack '{snack.snack_name}' added to the inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print(f"Snack with ID '{snack_id}' removed from the inventory.")
                return
        print(f"Snack with ID '{snack_id}' not found in the inventory.")

    def update_snack_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print(f"Snack with ID '{snack_id}' availability updated to '{availability}'.")
                return
        print(f"Snack with ID '{snack_id}' not found in the inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    snack.availability = "no"
                    self.sales_records.append(snack)
                    print(f"Snack with ID '{snack_id}' sold.")
                    return
                else:
                    print(f"Snack with ID '{snack_id}' is not available for sale.")
                    return
        print(f"Snack with ID '{snack_id}' not found in the inventory.")

    def display_inventory(self):
        print("Snack Inventory:")
        for snack in self.inventory:
            print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}, Availability: {snack.availability}")

    def display_sales_records(self):
        print("Sales Records:")
        for snack in self.sales_records:
            print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}")



def run_application():
    inventory = SnackInventory()

    while True:
        print("\nMenu:")
        print("1. Add Snack to Inventory")
        print("2. Remove Snack from Inventory")
        print("3. Update Snack Availability")
        print("4. Sell Snack")
        print("5. Display Inventory")
        print("6. Display Sales Records")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            snack_id = input("Enter snack ID: ")
            snack_name = input("Enter snack name: ")
            price = input("Enter snack price: ")
            availability = input("Enter snack availability (yes/no): ")
            snack = Snack(snack_id, snack_name, price, availability)
            inventory.add_snack(snack)

        elif choice == "2":
            snack_id = input("Enter snack ID: ")
            inventory.remove_snack(snack_id)

        elif choice == "3":
            snack_id = input("Enter snack ID: ")
            availability = input("Enter snack availability (yes/no): ")
            inventory.update_snack_availability(snack_id, availability)

        elif choice == "4":
            snack_id = input("Enter snack ID: ")
            inventory.sell_snack(snack_id)

        elif choice == "5":
            inventory.display_inventory()

        elif choice == "6":
            inventory.display_sales_records()

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

run_application()
