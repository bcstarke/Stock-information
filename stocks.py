import bs4
import requests
from bs4 import BeautifulSoup

#function to prompt user to enter ticker
def getStock():
    stock = input("Enter ticker: ")
    return str(stock.upper()) #converts input to upeprcase
     
def parsePrice():
    r = requests.get('https://finance.yahoo.com/quote/' + str(getStock()) + '/') 
    soup = bs4.BeautifulSoup(r.text, "xml")
    currentPrice = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text #parses yahoo finance XML for current price information
    return currentPrice

while True:
    print('The current price of ' + str(getStock()) + ' is ' + str(parsePrice()))
    
