import os

from selenium import webdriver

os.environ['PATH'] += r"C:/seleniumDrivers"

driver = webdriver.Chrome()
driver.get("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?5105e8233f9433cf70ac379d6ccc5775")
driver.implicitly_wait(10)

elements = driver.find_elements_by_class_name('html-attribute-value')

usdValue = float(elements[4].text)
todayDate = str(elements[2].text)

import csv

fields = ['Currency Code', 'Rate']

rows = []

for currencyPosition in range(5, len(elements), 2):
    currency = elements[currencyPosition].text
    value = float(elements[currencyPosition + 1].text)
    rows.append([f"{currency}", f"{(value/usdValue):.3f}"])

filename = "usd_currency_rates_{"+ todayDate +"}.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)

    csvwriter.writerows(rows)