from selenium import webdriver 
 
from selenium.webdriver.common.by import By 
import csv
import time 
 
driver = webdriver.Chrome() 
 
driver.get('https://www.startech.com.bd/product/search?&search=hp+laptop&page=1') 
 
driver.maximize_window() 
 
all_data = [] 
for page in range(1,3): 
    driver.get(f'https://www.startech.com.bd/product/search?&search=hp+laptop&page={page}')
 
    for i in range(1,16):
        try:
            xpath = f'//*[@id="content"]/div[2]/div[{i}]/div/div[2]/h4/a'
            laptop_name = driver.find_element(By.XPATH, xpath).text
            all_data.append(laptop_name)
        except:
            print(f"laptop at index {i} not found on page {page}")
       
file_name ="laptop_list.csv"
with open(file_name, "w", encoding="utf-8-sig", newline ="" ) as file:
    writer = csv.writer(file)
    for name in all_data:
        writer.writerow([name])

    print(f"Data saved to {file_name}")
 
 
print(all_data)
print(len(all_data))
time.sleep(10)
driver.quit() 