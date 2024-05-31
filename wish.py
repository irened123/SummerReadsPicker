from data import *
from outro import *

def view_wish_list():
    count = 1
    print()
    for key, value in wish_list.items():
        print(f"{count}. {key} by {value}")
        count += 1
    stop_view = False
    while (not stop_view): 
        user_input = str(input("\nType 'a' if you want to directly add a book/author, type 'd' if you want to delete a book, type 'n' if you don't want your wishlist to change!\n"))
        if (user_input == 'a'):
            direct_add()
        elif (user_input == 'd'):
            delete()
        else: 
            stop_view = True
    next_step = str(input("\nEnter 'y' to explore another genre, and enter 'n' to exit the program. :)\n"))
    if (next_step == 'n'):
        return True 
    else:
        return False 
        
    

def add_to_wish_list(genre, num_book):
    book_name = book_recommendations[genre][num_book]["name"]
    book_author = book_recommendations[genre][num_book]["author"]
    wish_list[book_name] = book_author

def direct_add():
    book_name = str(input("\nEnter the name of the book you want to add.\n"))
    book_author = str(input("\nEnter the author of the book you want to add.\n"))
    wish_list[book_name] = book_author 
    print("\nAll set!")
    
def delete(): 
    book_name = str(input("\nEnter the name of the book you want to delete.\n"))
    del wish_list[book_name]
    print("All set!")
    
    