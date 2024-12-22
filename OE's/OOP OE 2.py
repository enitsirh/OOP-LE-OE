class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

def modify_phone(phone):
    print(f"Modifying {phone}")
    phone.brand = input("Enter new brand: ")
    phone.model = input("Enter new model: ")
    phone.price = input("Enter new price: ")
    print("Phone details updated.")

def delete_phone_attributes(phone):
    print(f"Deleting attributes of {phone}")
    phone.brand = None
    phone.model = None
    phone.price = None
    print("Phone attributes deleted.")

def delete_phone(phone_list, index):
    if 0 <= index < len(phone_list):
        print(f"Deleting {phone_list[index]}")
        del phone_list[index]
        print("Phone deleted.")
    else:
        print("Invalid index.")

def main_menu():
    phones = []
    
    while True:
        print("\nMain Menu:")
        print("1. Add new phone")
        print("2. Modify phone")
        print("3. Delete phone attributes")
        print("4. Delete phone")
        print("5. View all phones")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            brand = input("Enter phone brand: ")
            model = input("Enter phone model: ")
            price = input("Enter phone price: ")
            phone = Phone(brand, model, price)
            phones.append(phone)
            print("Phone added successfully.")
        
        elif choice == '2':
            index = int(input("Enter the index of the phone to modify: "))
            if 0 <= index < len(phones):
                modify_phone(phones[index])
            else:
                print("Invalid index.")
        
        elif choice == '3':
            index = int(input("Enter the index of the phone to delete attributes: "))
            if 0 <= index < len(phones):
                delete_phone_attributes(phones[index])
            else:
                print("Invalid index.")
        
        elif choice == '4':
            index = int(input("Enter the index of the phone to delete: "))
            delete_phone(phones, index)
        
        elif choice == '5':
            if phones:
                index = 0
                for phone in phones:
                    print(f"{index}: {phone}")
                    index += 1
            else:
                print("No phones available.")
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()