import os #importing operal system

from selenium import webdriver #importing webdriver

os.environ['PATH'] += r"C:/seleniumDrivers" #opening the file that has my driver

driver = webdriver.Chrome() #opening chrome
driver.get("https://finance.yahoo.com/quote/BTC-EUR/history/") #open yahoo url
driver.implicitly_wait(10) #wait 10s for the page loading

#Get the all values through the false-element react-id
data1 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='51'] > td[data-reactid='52'] > span[data-reactid='53']")
close1 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='51'] > td[data-reactid='60'] > span[data-reactid='61']")

data2 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='66'] > td[data-reactid='67'] > span[data-reactid='68']")
close2 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='66'] > td[data-reactid='75'] > span[data-reactid='76']")

data3 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='81'] > td[data-reactid='82'] > span[data-reactid='83']")
close3 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='81'] > td[data-reactid='92'] > span[data-reactid='93']")

data4 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='96'] > td[data-reactid='97'] > span[data-reactid='98']")
close4 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='96'] > td[data-reactid='105'] > span[data-reactid='106']")

data5 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='111'] > td[data-reactid='112'] > span[data-reactid='113']")
close5 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='111'] > td[data-reactid='120'] > span[data-reactid='121']")

data6 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='126'] > td[data-reactid='127'] > span[data-reactid='128']")
close6 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='126'] > td[data-reactid='135'] > span[data-reactid='136']")

data7 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='141'] > td[data-reactid='142'] > span[data-reactid='143']")
close7 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='141'] > td[data-reactid='150'] > span[data-reactid='151']")

data8 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='156'] > td[data-reactid='157'] > span[data-reactid='158']")
close8 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='156'] > td[data-reactid='165'] > span[data-reactid='166']")

data9 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='171'] > td[data-reactid='172'] > span[data-reactid='173']")
close9 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='171'] > td[data-reactid='180'] > span[data-reactid='181']")

data10 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='186'] > td[data-reactid='187'] > span[data-reactid='188']")
close10 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='186'] > td[data-reactid='195'] > span[data-reactid='196']")

import csv

fields = ['Date', 'BTC Closing Value'] # name for columns

#writing lines
rows = [
    [f"{data1.text}", f"{close1.text}"],
    [f"{data2.text}", f"{close2.text}"],
    [f"{data3.text}", f"{close3.text}"],
    [f"{data4.text}", f"{close4.text}"],
    [f"{data5.text}", f"{close5.text}"],
    [f"{data6.text}", f"{close6.text}"],
    [f"{data7.text}", f"{close7.text}"],
    [f"{data8.text}", f"{close8.text}"],
    [f"{data9.text}", f"{close9.text}"],
    [f"{data10.text}", f"{close10.text}"]
]
#create with the name eur_btc_rates.csv and writing the values to columns and lines
with open("eur_btc_rates.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)

    csvwriter.writerows(rows)