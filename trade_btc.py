import balance
import requests
from bs4 import BeautifulSoup
import Bitcoin_balance
import random
import shutil
import os
import tran




def Start(AUD):
    files = open('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/files/tran.txt', 'a')
    files.write(f'Starting_Balance = {AUD}\n')
    files.close()
    ## Starting Balance
    Starting_Balance = AUD
    balance.starting(Starting_Balance)

    ## Starting Bitcoin Balance
    Starting_Bitcoin_Balance = float(0.0000000000000)
    Bitcoin_balance.starting(Starting_Bitcoin_Balance)

    start = (f'Starting balance: ${AUD}')
    print (start)
    return start

def Bitcoin_Price():
    URL = 'https://au.finance.yahoo.com/quote/BTC-AUD/'
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(name=None, attrs={'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}, recursive=True, text=None).text
    replace = title.replace(",","")
    price = float(replace)
    return price

def Buy(How_much_AUD):
    Balance = balance.Balance()
    math = How_much_AUD - Balance
    price = Bitcoin_Price()
    if How_much_AUD == 'all':
        math = Balance
    if math <= 0.01:
        bitcoin_amount = (How_much_AUD/price)
        Bitcoin_balance.add(bitcoin_amount)
        balance.subcract(How_much_AUD)

        id = (tran_id())
        tran_str = (f'[Buy: {bitcoin_amount}, Bitcoin Price: {price}, Value: {How_much_AUD}]')
        tran = (f'[{bitcoin_amount}, {price}, {How_much_AUD}]')
        files = open('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/files/tran.txt', 'a')
        files.write(f'Buy_{id} = {tran_str}\n')
        files.close()

        filess = open('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/tran.py', 'a')
        filess.write(f'    if id == {id}:\n')
        filess.write(f'        tran = {tran}\n')
        filess.write(f'        tran0 = tran[0]\n')
        filess.write(f'        tran1 = tran[1]\n')
        filess.write(f'        tran2 = tran[2]\n')
        filess.write(f'        if trans == "tran":\n')
        filess.write(f'            return tran\n')
        filess.write(f'        if trans == "tran0":\n')
        filess.write(f'            return tran0\n')
        filess.write(f'        if trans == "tran1":\n')
        filess.write(f'            return tran1\n')
        filess.write(f'        if trans == "tran2":\n')
        filess.write(f'            return tran2\n')
        filess.close()
        print(tran_str)
        print(f'ID: {id}')
        return tran_str
    else:
        print('Not Enough Funds')




def Sell(How_much_BTC):
    btc_balance = Bitcoin_balance.Balance()
    math = How_much_BTC - btc_balance
    if How_much_BTC == 'all':
        math = btc_balance
    if math <= 0.0000000000000001:
        price = Bitcoin_Price()
        value = price*How_much_BTC

        Bitcoin_balance.subcract(How_much_BTC)
        balance.add(value)

        id = (tran_id())

        tran_str = (f'[Sell: {How_much_BTC}, Bitcoin Price: {price}, Value: {value}]')
        files = open('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/files/tran.txt', 'a')
        files.write(f'Sell_{id} = {tran_str}\n')
        files.close()
    else:
        print('Not Enough Funds')
        return 'Not Enough Funds'


def Balance_Value():
    Bitcoin_Amount = Bitcoin_balance.Balance()
    BTC_Price = Bitcoin_Price()
    Value = float(Bitcoin_Amount*BTC_Price)
    print(f'Bitcoin Value: ${Value}')
    return Value

def Profit_Loss(tran_id):
    Bitcoin_Amount = tran.tran(tran_id, 'tran0')
    BTC_Price = Bitcoin_Price()
    Value = float(Bitcoin_Amount*BTC_Price)
    Start_Value = tran.tran(tran_id, 'tran2')
    Profit_Loss = (Value-Start_Value)
    
    prints = (f'Starting Value: {Start_Value}')
    prints2 = (f'Current Value: {Value}')
    prints12 = (f'Profit/Loss: {Profit_Loss}')
    returns = (f'{prints} {prints} {prints12}')
    print(prints)
    print(prints2)
    print(prints12)
    return returns



def tran_print():
    file = open('tran.py', 'r')
    file = (file.read())
    print(file)
    return file


def tran_id():
    keygen = (random.randint(111111, 999999))
    return keygen

def reset():
    os.remove('trade_btc.py')
    os.remove('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/files/Balance.txt')
    os.remove('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/files/BTC_Balance.txt')
    os.remove('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/files/tran.txt')
    os.remove('tran.py')
    shutil.copy2('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/reset/trade_btc.py', '/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/trade_btc.py')
    shutil.copy2('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/reset/tran.py', '/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/tran.py')

def Cheek_Bitcoin_Balance():
    balance = Bitcoin_balance.Balance()
    print(balance)
    return balance

def Cheek_Balance():
    bal = balance.Balance()
    print(bal)
    return bal


def add_balance(amount):
    files = open('/Users/nikola/Documents/Other/VisualStudioCode/Playing/Bank/files/tran.txt', 'a')
    files.write(f'Add_Balance = {amount}\n')
    files.close()
    balance.add(amount)


