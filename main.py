#Amazon web scrapper using python

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options)

URL = 'https://www.amazon.com/Cyberpunk-2077-PC/dp/B07T8BP118/ref=sr_1_2?crid=1QENYTQKIKIZ2&dchild=1&keywords=cyberpunk+2077+pc&qid=1602002101&sprefix=cyberpunk+2077+%2Caps%2C191&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'}

def check_price():
    driver.get(URL)
    page = driver.page_source

    soup = BeautifulSoup(page, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:-3])

    print(converted_price)

    driver.quit()

print(check_price())