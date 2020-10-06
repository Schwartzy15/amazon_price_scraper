#Amazon web scrapper using python

import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Cyberpunk-2077-PC/dp/B07T8BP118/ref=sr_1_2?' \
      'crid=1QENYTQKIKIZ2&dchild=1&keywords=cyberpunk+2077+pc&' \
      'qid=1602002101&sprefix=cyberpunk+2077+%2Caps%2C191&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 '
                         'Firefox/81.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
