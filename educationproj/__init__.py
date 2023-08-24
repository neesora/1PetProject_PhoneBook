phone_book = {}

def add_contact():
    name = input("Write name: ")
    nickname = input("Write nickname: ")
    number = input("Write number: ")
    phone_book[name] = {"Nickname":nickname, "Number":number}

def modify_contact():
    name = input("Write the exist name of contact which will edit: ")
    while name == "":
        name = input("Write something")
    if name in phone_book:
        nickname = input("Write new nickname: ")
        while nickname == "":
            break
        number = input("Write new number: ")
        while number == "":
            break
    modifying = phone_book[name] #this block needed for replacement exist values to new values
    if nickname:
        modifying["Nickname"] = nickname
    if number:
        modifying["Number"] = number
    else:
        print("Contact was not found")
def delete_contact():
    name = input("Write the exist name of contact which will delete: ")
    if name in phone_book:
        del phone_book[name]
    else:
        print("Contact was not found")
#def show_contacts():


def main():
    while True:
        print("Phone book")
        print("Write 1 to add new contact.")
        print("Write 2 to modify exist contact.")
        print("Write 3 to delete contact.")
        print("Write 4 to show contacts.")
        print("Write 5 to stop running.")
        choice = input("Enter choice ")
        if choice == "1":
            add_contact()
        if choice == "2":
            modify_contact()
        if choice == "3":
            delete_contact()
        if choice == "4":
            print(phone_book)
        if choice == "5":
            break
        else:
            print("That's option isn't exist.")
if __name__ == "__main__":
    main()
