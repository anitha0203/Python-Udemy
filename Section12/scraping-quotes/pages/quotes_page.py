# from locators.quotes_page_locators import QuotesPageLocators
# from parsers.quote import QuoteParser
#
#
# class QuotesPage:
#     def __init__(self, browser):
#         self.browser = browser
#
#     @property
#     def quotes(self):
#         locator = QuotesPageLocators.QUOTE
#         quote_tags = self.browser.find_elements_by_css_selector(locator)
#         return [QuoteParser(e) for e in quote_tags]


from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser
from selenium.webdriver.common.by import By


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(e) for e in quote_tags]
