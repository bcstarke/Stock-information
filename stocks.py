import bs4
import requests
from bs4 import BeautifulSoup

def getStock():
    stock = input("Enter ticker: ")
    return str(stock.upper())
   
def parsePrice():
    #parsePrice.stock = input("Enter ticker: ")
    r = requests.get('https://finance.yahoo.com/quote/' + str(getStock()) + '/')
    soup = bs4.BeautifulSoup(r.text, "xml")
    currentPrice = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return currentPrice

while True:
    print('The current price of ' + str(getStock()) + ' is ' + str(parsePrice()))
    