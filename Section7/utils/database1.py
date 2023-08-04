
books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)

    # books = [book for book in books if book['name'] != name]