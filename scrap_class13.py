from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()#client
driver.get('https://www.daraz.com.bd/products/')

driver.maximize_window()
time.sleep(10)