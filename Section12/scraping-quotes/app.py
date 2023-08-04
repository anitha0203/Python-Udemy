# from selenium import webdriver
#
# from pages.quotes_page import QuotesPage
#
# chrome = webdriver.Chrome(executable_path="D:/Anitha/Softwares/chromedriver_win32")
# chrome.get("http://quotes.toscrape.com")
# page = QuotesPage(chrome)
#
# for quote in page.quotes:
#     print(quote.content)

from selenium import webdriver
from pages.quotes_page import QuotesPage

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("executable_path=D:/Anitha/Softwares/chromedriver_win32/chromedriver.exe")
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("http://quotes.toscrape.com")
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote.content)

