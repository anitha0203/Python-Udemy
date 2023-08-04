from bs4 import BeautifulSoup

from locators.books_page_locators import BooksPageLocators
from parsers.books import BooksParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def content(self):
        locator = BooksPageLocators.BOOK
        book_title = self.soup.select(locator)
        return [BooksParser(e) for e in book_title]

    @property
    def link(self):
        locator = BooksPageLocators.BOOK
        book_title = self.soup.select(locator)
        return [BooksParser(e) for e in book_title]

    @property
    def price(self):
        locator = BooksPageLocators.BOOK
        book_title = self.soup.select(locator)
        return [BooksParser(e) for e in book_title]

    # @property
    # def books(self):
    #     return [BooksParser(e) for e in self.soup.select(BooksPageLocators.BOOK)]
