
def create_book_table():
    with open('books.txt', 'a'):
        pass


def add_book(name, author):
    with open('books.txt', 'a') as file:
        file.write(f'{name},{author},0\n')


def get_all_books():
    with open('books.txt', 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    books = [{
        'name': line[0], 'author': line[1], 'read': line[2]
    }for line in lines]
    return books


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    with open('books.txt', 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}")


def delete_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            books.remove(book)
    with open('books.txt', 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}")

