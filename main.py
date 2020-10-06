# Amazon web scrapper using python

import requests
import time
import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options)

URL = 'https://www.amazon.com/Cyberpunk-2077-PC/dp/B07T8BP118/ref=sr_1_2?' \
      'crid=1QENYTQKIKIZ2&dchild=1&keywords=cyberpunk+2077+pc&qid=1602002101&' \
      'sprefix=cyberpunk+2077+%2Caps%2C191&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) '
                         'Gecko/20100101 Firefox/81.0'}

with open('email.config') as f:
    credentials = [line.rstrip() for line in f]


def check_price():
    driver.get(URL)
    page = driver.page_source

    soup = BeautifulSoup(page, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:-3])

    if converted_price > 50:
        send_mail()
        driver.quit()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(credentials[0], credentials[1])

    subject = 'Price Increased! Cyberpunk 2077 - PC'
    body = 'Check link: https://www.amazon.com/Cyberpunk-2077-PC/dp/B07T8BP118/ref=sr_1_2?' \
           'crid=1QENYTQKIKIZ2&dchild=1&keywords=cyberpunk+2077+pc&qid=1602002101&' \
           'sprefix=cyberpunk+2077+%2Caps%2C191&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(credentials[0], credentials[0], msg)
    print("EMAIL SENT")

    server.quit()


while True:
    check_price()
    time.sleep(3600)
