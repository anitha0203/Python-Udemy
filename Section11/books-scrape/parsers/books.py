from locators.book_locators import BOOKLocators


class BooksParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.content}, price {self.price}, link {self.link}>'

    @property
    def content(self):
        locator = BOOKLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def link(self):
        locator = BOOKLocators.SRC
        return self.parent.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = BOOKLocators.PRICE
        return self.parent.select_one(locator).string

