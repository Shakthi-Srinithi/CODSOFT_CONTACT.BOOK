class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def search_contact(self, query):
        for name, details in self.contacts.items():
            if query in name or query in details['phone']:
                print(f"Found: {name}, Phone: {details['phone']}")
                return
        print("No contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone: self.contacts[name]['phone'] = phone
            if email: self.contacts[name]['email'] = email
            if address: self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            name = input("Enter the name to update: ")
            phone = input("New phone (leave blank to skip): ")
            email = input("New email (leave blank to skip): ")
            address = input("New address (leave blank to skip): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None, address if address else None)

        elif choice == '5':
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
