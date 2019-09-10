import bs4
import requests
from bs4 import BeautifulSoup

# XML code that contains price of stock on yahoo finance
STOCK_PRICE_WINDOW = 'My(6px) Pos(r) smartphone_Mt(6px)'
# XML code that contains price of crypto on yahoo finance
CRYPTO_PRICE_WINDOW = 'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'
# All quotes referenced from this URL. Made global to cut down repeat code
YAHOO_URL = 'https://finance.yahoo.com/quote/'

# class which creates Stock object
class Stock:
    def __init__(self, stock):
        self.stock = stock
        self.price = requests.get(YAHOO_URL + str(stock) + '/')
        self.soup = bs4.BeautifulSoup(self.price.text, "xml")

    # parses XML of inputted ticker webpage to return current price.
    # Can accept upper or lower case input
    def parse_price(self, stock):
        stock_price = self.soup.find('div', {'class': STOCK_PRICE_WINDOW}).find('span').text
        return stock_price

# class which creates Dow Jones object.
class DJIA:
    def __init__(self):
        self.price = requests.get(YAHOO_URL + '%5EDJI?p=^DJI')
        self.soup = bs4.BeautifulSoup(self.price.text, "xml")

    # parses XML of DJIA webpage to return current price.
    def get_DJIA_price(self):
        dow_price = self.soup.find('div', {'class': STOCK_PRICE_WINDOW}).find('span').text
        return dow_price

    # neatly prints current DJIA price to terminal
    def print_DJIA(self):
        return "DJIA: " + self.get_DJIA_price()

class SP500:
    def __init__(self):
        self.price = requests.get(YAHOO_URL + '%5EGSPC?p==^GSPC')
        self.soup = bs4.BeautifulSoup(self.price.text, "xml")

    def get_sp500_price(self):
        sp500_price = self.soup.find('div', {'class': STOCK_PRICE_WINDOW}).find('span').text
        return sp500_price

    def print_SP500(self):
        return "S&P500: " + self.get_sp500_price()

class Nasdaq:
    def __init__(self):
        self.price = requests.get(YAHOO_URL + '%5EIXIC?p=^IXIC')
        self.soup = bs4.BeautifulSoup(self.price.text, "xml")

    def get_nasdaq_price(self):
        nasdaq_price = self.soup.find('div', {'class': STOCK_PRICE_WINDOW}).find('span').text
        return nasdaq_price

    def print_nasdaq(self):
        return "Nasdaq: " + self.get_nasdaq_price()

class Bitcoin:
    def __init__(self):
        self.price = requests.get(YAHOO_URL + 'BTC-USD?p=BTC-USD')
        self.soup = bs4.BeautifulSoup(self.price.text, "xml")

    def get_bitcoin_price(self):
        bitcoin_price = self.soup.find('div', {'class': CRYPTO_PRICE_WINDOW}).find('span').text
        return bitcoin_price

    def print_bitcoin_price(self):
        return 'Bitcoin: ' + self.get_bitcoin_price() #+ 'Market cap: ' + self.get_BTC_market_cap()

class Ether:
    def __init__(self):
        self.price = requests.get(YAHOO_URL + 'ETH-USD?p=ETH-USD')
        self.soup = bs4.BeautifulSoup(self.price.text, "xml")

    def get_ether_price(self):
        ether_price = self.soup.find('div', {'class': CRYPTO_PRICE_WINDOW}).find('span').text
        return ether_price

    def print_ether_price(self):
        return "Ethereum: " + self.get_ether_price()

class Ripple:
    def __init__(self):
        self.price = requests.get(YAHOO_URL + 'XRP-USD?p=XRP-USD')
        self.soup = bs4.BeautifulSoup(self.price.text, "xml")

    def get_ripple_price(self):
        ripple_price = self.soup.find('div', {'class': CRYPTO_PRICE_WINDOW}).find('span').text
        return ripple_price

    def print_ripple_price(self):
        return "Ripple: " + self.get_ripple_price()

def main():
    # Create index objects
    dow = DJIA()
    sp500 = SP500()
    nasdaq = Nasdaq()

    # Create crypto objects
    btc = Bitcoin()
    eth = Ether()
    rip = Ripple()

    # Output current US Equity markets to the terminal
    print("====== US Equity Markets Right Now ===== ")
    print(dow.print_DJIA() + '\n' + sp500.print_SP500() + '\n' + nasdaq.print_nasdaq() + '\n')

    # Output current crypto currency markets to the terminal
    print("=== Crypto currency Markets Right Now === ")
    print(btc.print_bitcoin_price() + '\n' + eth.print_ether_price() + '\n' + rip.print_ripple_price() + '\n')

    # Prompt user to enter a ticker
    input_stock = str(input("Enter ticker: ")).upper()

    # Create equity object with input_stock as argument
    equity = Stock(input_stock)
    try:
        print('The current price of ' + input_stock + ' is ' + equity.parse_price(input_stock))
    except:
        print("Symbol not found")
main()
