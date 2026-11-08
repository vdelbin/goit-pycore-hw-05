from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "show_phone":
                return "Enter only one user name."
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."

    return inner

def parse_input(user_input):
    parts = user_input.lower().split()

    if not parts:
        return "", []

    command = parts[0]
    args = parts[1:]
    return command, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        raise KeyError(name)

    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]

    if len(args) != 1:
        raise ValueError

    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."

    lines = []

    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")

    return "\n".join(lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"] and not args:
            print("Good bye!")
            break
        elif command == "hello" and not args:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all" and not args:
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()