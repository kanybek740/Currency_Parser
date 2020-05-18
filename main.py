import requests
from bs4 import BeautifulSoup
import time

DOLLAR_RUB = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}

def check_currency():

    full_page = requests.get(DOLLAR_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll('td', {'class': 'stat-left'})
    print('Eto kurs nach banka = ' + convert[0].text)
    time.sleep(5)
    check_currency()
check_currency()
