'''
Created on Mar 15, 2020

@author: cmwat
'''

import urllib.request
import json

'''
print('calling nasdaq')
nasdaqAppleURL = 'https://www.nasdaq.com/symbol/aapl'
connection = urllib.request.urlopen(nasdaqAppleURL)
responseString = connection.read().decode()

print(responseString)

print('calling alphaadvantage')
alphaavantage = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=O3AKXQQLD1HWUI5B'
connection2 = urllib.request.urlopen(alphaavantage)
responseString2 = connection2.read().decode()

print(responseString2)'''

def getStockData():
    while True:
        symbol = input("Enter a stock symbol: ")
        if symbol == 'quit':
            break
        else: 
            print('calling alphaadvantage 2')
#alphaavantage2 = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbol=AAPL&apikey=O3AKXQQLD1HWUI5B'
            alphaavantage2 = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=O3AKXQQLD1HWUI5B'
            connection3 = urllib.request.urlopen(alphaavantage2)
            responseString3 = connection3.read().decode()
            print(responseString3)
            
            alpha_dump = json.dumps(responseString3)
            print(alpha_dump)
            
            alpha_dict = json.loads(alpha_dump)
            f=open("japi.out", "a+")
            f.write(alpha_dict)
            
            print(alpha_dict)
            

getStockData()
