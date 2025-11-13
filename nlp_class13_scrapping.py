from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('https://www.daraz.com.bd/mens-sneakers')
driver.maximize_window()
text_list=[]
for x in range(1,3):
    j=str(x)
  
    text=driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span['+j+']').text
    text_list.append(text)

print(text_list)

time.sleep(20)