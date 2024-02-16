from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number")
        super().__init__(value)

class Email(Field):
    def __init__(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_email(self, email):
        self.emails.append(Email(email))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def remove_email(self, email):
        self.emails = [e for e in self.emails if str(e) != email]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def edit_email(self, old_email, new_email):
        self.remove_email(old_email)
        self.add_email(new_email)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        emails_str = '; '.join(str(email) for email in self.emails)
        return f"Contact name: {self.name.value}, phones: {phones_str}, emails: {emails_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, query):
        deleted = False
        
        if "@" in query or query.isdigit():
            # Удаляем номер телефона или почту из всех контактов
            for record in self.data.values():
                if any(query == str(phone) for phone in record.phones) or any(query == str(email) for email in record.emails):
                    record.remove_phone(query)
                    record.remove_email(query)
                    deleted = True
        else:
            # Удаляем контакт по имени
            if query in self.data:
                del self.data[query]
                deleted = True

        if deleted:
            return f"Contact with phone number, email or name '{query}' deleted."
        else:
            return f"Contact with phone number, email or name '{query}' not found."

    def search(self, query):
        results = []
        for record in self.data.values():
            if record.name.value.lower() == query.lower():
                results.append(record)
            for phone in record.phones:
                if str(phone) == query:
                    results.append(record)
            for email in record.emails:
                if str(email) == query:
                    results.append(record)
        return results

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, address_book):
    name, *info = args
    record = address_book.find(name)
    if record:
        for item in info:
            if "@" in item:
                record.add_email(item)
            else:
                record.add_phone(item)
        return f"Contact '{name}' updated with additional info."
    else:
        record = Record(name)
        for item in info:
            if "@" in item:
                record.add_email(item)
            else:
                record.add_phone(item)
        address_book.add_record(record)
        return f"New contact '{name}' added with phone number(s) and email(s)."

def show_all(args, address_book):
    if not args:
        if not address_book.data:
            return "There are no contacts yet."
        return "\n".join([str(record) for record in address_book.data.values()])
    else:
        return "Invalid command. Usage: all"

def find_contact(args, address_book):
    query = args[0]
    results = address_book.search(query)
    if results:
        return "\n".join([str(record) for record in results])
    else:
        return f"No contacts found for query '{query}'."

def delete_contact(args, address_book):
    query = args[0]
    deleted = False
    
    if "@" in query or query.isdigit():
        # Удаляем номер телефона или почту из всех контактов
        for record in address_book.data.values():
            if any(query == str(phone) for phone in record.phones) or any(query == str(email) for email in record.emails):
                record.remove_phone(query)
                record.remove_email(query)
                deleted = True
    else:
        # Удаляем контакт по имени
        if query in address_book.data:
            del address_book.data[query]
            deleted = True

    if deleted:
        return f"Contact with phone number, email or name '{query}' deleted."
    else:
        return f"Contact with phone number, email or name '{query}' not found."

def change_contact(args, address_book):
    name, *phones_or_emails = args
    records = address_book.search(name)
    if records:
        for record in records:
            for item in phones_or_emails:
                if "@" in item:
                    record.edit_email(record.emails[0].value, item)
                else:
                    record.edit_phone(record.phones[0].value, item)
        return f"Contact '{name}' updated with additional info."
    else:
        return f"Contact with name '{name}' not found."

def main():
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, address_book))
        elif command == "all":
            print(show_all(args, address_book))
        elif command == "find":
            print(find_contact(args, address_book))
        elif command == "delete":
            print(delete_contact(args, address_book))
        elif command == "change":
            print(change_contact(args, address_book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



#hello:  Вивести привітальне повідомлення.
#add:  Додати новий контакт у адресну книгу. (Ім'я, номер, пошту)
#change:  Змінити номер телефону, пошту у вказаному контакті.
#all:  Показати всі контакти у книзі.
#find:  Знайти контакт за ім'ям або номером телефону або поштою.
#delete: Видалити вказаний контакт із книги, або номер чи пошту із контакту.
#close:  Закрити бота.
#exit:  Вийти з бота.