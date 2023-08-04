from .db1 import DatabaseConnection


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('select * from books')

        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # {'name': 'mf', 'author': 0, 'read': 0}
    return books


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('insert into books values(?, ?, 0)', (name, author))


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('update books set read=1 where name = ?', (name,))


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('delete from books where name = ?', (name,))










# import sqlite3
#
#
# books_file = 'books.json'
#
#
# def create_book_table():
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
#
#     cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
#
#     connection.commit()
#     connection.close()
#
#
# def get_all_books():
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
#
#     cursor.execute('select * from books')
#     # books = cursor.fetchall()         #   ('mf', 0, 0)
#     books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # {'name': 'mf', 'author': 0, 'read': 0}
#
#     connection.close()
#
#     return books
#
#
# def add_book(name, author):
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
#
#     # cursor.execute(f'insert into books values("{name}", "{author}", 0)')
#
#     cursor.execute('insert into books values(?, ?, 0)', (name, author))
#
#     connection.commit()
#     connection.close()
#
#
# def mark_book_as_read(name):
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
#
#     cursor.execute('update books set read=1 where name = ?', (name,))
#
#     connection.commit()
#     connection.close()
#
#
# def delete_book(name):
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
#
#     cursor.execute('delete from books where name = ?', (name,))
#
#     connection.commit()
#     connection.close()
