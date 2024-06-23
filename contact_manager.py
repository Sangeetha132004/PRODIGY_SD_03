import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

class ContactManager:
    def __init__(self, filepath='contacts.json'):
        self.filepath = filepath
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_contacts(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact.to_dict())
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def search_contact(self, search_term):
        found_contacts = [c for c in self.contacts if search_term.lower() in c['name'].lower()]
        if not found_contacts:
            print("No matching contacts found.")
            return
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def update_contact(self, search_term, new_name=None, new_phone=None, new_email=None):
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower():
                if new_name:
                    contact['name'] = new_name
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                self.save_contacts()
                print("Contact updated successfully!")
                return
        print("No matching contacts found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully!")
                return
        print("No matching contacts found.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name to update: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            manager.update_contact(search_term, new_name, new_phone, new_email)
        elif choice == '5':
            search_term = input("Enter name to delete: ")
            manager.delete_contact(search_term)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
