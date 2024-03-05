import pickle

class Contact:
    def __init__(self, name, email, phone, favorite=False):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def show_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print("Name:", contact.name)
                print("Email:", contact.email)
                print("Phone:", contact.phone)
                print("Favorite:", contact.favorite)
                print()
        else:
            print("Address book is empty.")

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    while True:
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Show contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            favorite = input("Is this contact favorite? (yes/no): ").lower() == "yes"
            contact = Contact(name, email, phone, favorite)
            book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            name = input("Enter name of contact to remove: ")
            if book.remove_contact(name):
                print("Contact removed successfully!")
            else:
                print("Contact not found!")

        elif choice == "3":
            book.show_contacts()

        elif choice == "4":
            save_data(book)
            print("Address book saved. Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
