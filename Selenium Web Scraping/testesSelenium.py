import os

from selenium import webdriver

os.environ['PATH'] += r"C:/seleniumDrivers"

driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/quote/BTC-EUR/history/")
driver.implicitly_wait(10)


data01 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='51'] > td[data-reactid='52'] > span[data-reactid='53']")
close01 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='51'] > td[data-reactid='60'] > span[data-reactid='61']")

data02 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='66'] > td[data-reactid='67'] > span[data-reactid='68']")
close02 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='66'] > td[data-reactid='75'] > span[data-reactid='76']")

data03 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='81'] > td[data-reactid='82'] > span[data-reactid='83']")
close03 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='81'] > td[data-reactid='92'] > span[data-reactid='93']")

data04 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='96'] > td[data-reactid='97'] > span[data-reactid='98']")
close04 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='96'] > td[data-reactid='105'] > span[data-reactid='106']")

data05 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='111'] > td[data-reactid='112'] > span[data-reactid='113']")
close05 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='111'] > td[data-reactid='120'] > span[data-reactid='121']")

data06 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='126'] > td[data-reactid='127'] > span[data-reactid='128']")
close06 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='126'] > td[data-reactid='135'] > span[data-reactid='136']")

data07 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='141'] > td[data-reactid='142'] > span[data-reactid='143']")
close07 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='141'] > td[data-reactid='150'] > span[data-reactid='151']")

data08 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='156'] > td[data-reactid='157'] > span[data-reactid='158']")
close08 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='156'] > td[data-reactid='165'] > span[data-reactid='166']")

data09 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='171'] > td[data-reactid='172'] > span[data-reactid='173']")
close09 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='171'] > td[data-reactid='180'] > span[data-reactid='181']")

data10 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='186'] > td[data-reactid='187'] > span[data-reactid='188']")
close10 = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section[data-reactid='2'] > div[data-reactid='32'] > table[data-reactid='33'] > tbody[data-reactid='50'] > tr[data-reactid='186'] > td[data-reactid='195'] > span[data-reactid='196']")

import csv

fields = ['Date', 'BTC Closing Value']

rows = [
    [f"{data01.text}", f"{close01.text}"],
    [f"{data02.text}", f"{close02.text}"],
    [f"{data03.text}", f"{close03.text}"],
    [f"{data04.text}", f"{close04.text}"],
    [f"{data05.text}", f"{close05.text}"],
    [f"{data06.text}", f"{close06.text}"],
    [f"{data07.text}", f"{close07.text}"],
    [f"{data08.text}", f"{close08.text}"],
    [f"{data09.text}", f"{close09.text}"],
    [f"{data10.text}", f"{close10.text}"]
]

with open("eur_btc_rates.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)

    csvwriter.writerows(rows)