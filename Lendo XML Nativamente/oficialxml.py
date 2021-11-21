from urllib import request


url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?5105e8233f9433cf70ac379d6ccc5775'

html = request.urlopen(url)
data = html.read()


from bs4 import BeautifulSoup
content = BeautifulSoup(data, 'html.parser')

todayDate = content.cube.cube['time']
todayDollar = float(content.cube.cube.cube['rate'])

arrCurrency = content.find_all(currency=True)


import csv

fields = ['Currency Code', 'Rate']

rows = []

for currency in arrCurrency:
    value = float(currency['rate'])
    rows.append([f"{currency['currency']}", f"{(value / todayDollar):.3f}"])

filename = "usd_currency_rates_{" + todayDate + "}.csv"

with open(filename, 'w') as csvfile:
     csvwriter = csv.writer(csvfile)

     csvwriter.writerow(fields)

     csvwriter.writerows(rows)