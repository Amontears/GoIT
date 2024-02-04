def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command. Usage: add [name] [phone]"

def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return f"Contact with name '{name}' not found."
    else:
        return "Invalid command. Usage: change [name] [phone]"

def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"Number for contact '{name}': {contacts[name]}."
        else:
            return f"Contact with name '{name}' not found."
    else:
        return "Invalid command. Usage: phone [name]"

def show_all(args, contacts):
    if not args:
        return contacts
    else:
        return "Invalid command. Usage: all"

def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
