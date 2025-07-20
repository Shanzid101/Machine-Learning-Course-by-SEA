
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://bikroy.com/')

driver.maximize_window()




   
title = driver.find_element(By.XPATH,'//*[@id="app-wrapper"]/div[1]/div[3]/div[4]/ul/li[1]/a/div[2]').text 
       



print(title)
time.sleep(10)
driver.quit()
  