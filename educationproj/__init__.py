phone_book = {}

def add_contact():
    name = input("Write name: ")
    nickname = input("Write nickname: ")
    number = input("Write number: ")
    phone_book[name] = {"Nickname":nickname, "Number":number}

def modify_contact():
    name = input("Write the exist name: ")
    if name in phone_book:
        #phone_book["nickname"] = input("Write new nickname") here I'm not sure work that or not and left it for tomorrow
        #phone_book["number"] = input("Write new number") 
    #else:
        #print("Name not in the book")
#choice = input("Text ")
#if choice == 1:
    #print(phone_book.items()) here I trynna test but tired and stopped
