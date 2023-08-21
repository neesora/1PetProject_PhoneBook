phone_book = {}

def add_contact():
    name = input("Write name: ")
    nickname = input("Write nickname: ")
    number = input("Write number: ")
    phone_book[name] = {"Nickname":nickname, "Number":number}


 