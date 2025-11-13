from selenium import webdriver
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Daraz
driver.get("https://www.daraz.com.bd")
driver.maximize_window()
time.sleep(10)
