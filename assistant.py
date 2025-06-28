from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Index of arguments is out of range"
        except KeyError:
            return "The name does not exists!"
        except ValueError:
            return "Enter correct number of arguments, please: name and phone."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split() 
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args    
    contacts[name] = phone
    
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact updated."

def show_all(contacts):
    return contacts

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError("Index of arguments is out of range")
    username = args[0]
    return contacts[username]
    
def main():
    contacts = {}
    print("Welcome to the assistent bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()