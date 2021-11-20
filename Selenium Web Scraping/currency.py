import os

from selenium import webdriver

os.environ['PATH'] += r"C:/seleniumDrivers"

driver = webdriver.Chrome()
driver.get("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?5105e8233f9433cf70ac379d6ccc5775")
driver.implicitly_wait(10)

elements = driver.find_elements_by_class_name('html-attribute-value')

usdValue = float(elements[4].text)

for currencyPosition in range(5, len(elements), 2):
    currency = elements[currencyPosition].text
    value = float(elemen ts[currencyPosition + 1].text)
    print(f"Currency: {currency}  Value: {value/usdValue}")