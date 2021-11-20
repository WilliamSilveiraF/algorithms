import os
from selenium import webdriver

os.environ['PATH'] += r"C:/seleniumDrivers"

driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/quote/BTC-EUR/history/")
driver.implicitly_wait(30)
#my_element = driver.find_element_by_id("header-desktop-search-button")
#my_element.click()
my_answer = driver.find_element_by_css_selector("#Col1-1-HistoricalDataTable-Proxy > section > div > table > tbody > tr > td > span[data-reactid='61']")
print(my_answer.text)