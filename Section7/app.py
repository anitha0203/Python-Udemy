# from utils import database
# from utils import database_json
from utils import db

USER_CHOICE = """
    Enter: 
    - 'a' to add a new book
    - 'l' to list all book
    - 'r' to mark a book as read
    - 'd' to delete a book
    - 'q' to quit

Your choice: """


def menu():
    db.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter the new book name: ")
    author = input("Enter the new book author: ")

    db.add_book(name, author)


def list_books():
    books = db.get_all_books()
    for book in books:
        print(book)


def prompt_read_book():
    name = input("Enter the name of the book you just finished reading: ")
    db.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter name of the book you wish to delete: ")

    db.delete_book(name)


menu()