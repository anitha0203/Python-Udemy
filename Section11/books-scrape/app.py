import requests

from pages.books_page import BooksPage

page_content = requests.get('https://books.toscrape.com/').content
page = BooksPage(page_content)

for book in page.content:
    print(book)

# for book in page.link:
#     print(book.link)
#
# for book in page.price:
#     print(book.price)
