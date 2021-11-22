#importing urllib to open the XML URL
from urllib import request


url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?5105e8233f9433cf70ac379d6ccc5775'

html = request.urlopen(url) #opening my url
data = html.read() #reading my url

#Importing Beautiful Soup Package to create my xml tree
from bs4 import BeautifulSoup
content = BeautifulSoup(data, 'html.parser')

todayDate = content.cube.cube['time'] #Get the today date
todayDollar = float(content.cube.cube.cube['rate']) #Get today’s dollar

arrCurrency = content.find_all(currency=True) #List of all elements in my tree that have the currency property


import csv

fields = ['Currency Code', 'Rate'] #Defining columns

rows = [] #Creating a list of empty lines

for currency in arrCurrency:
    value = float(currency['rate']) #Transforming my ratio value to float
    rows.append([f"{currency['currency']}", f"{(value / todayDollar):.3f}"]) #Looping all lines in the template: currency type and currency/dollar ratio

#According to the date of the last possible quote on the ECB website, format the date
filename = "usd_currency_rates_{" + todayDate + "}.csv"

#Creating the csv file and writing columns and rows
with open(filename, 'w') as csvfile:
     csvwriter = csv.writer(csvfile)

     csvwriter.writerow(fields)

     csvwriter.writerows(rows)