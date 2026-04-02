from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1,20):
 
  driver.get(f"https://www.amazon.in/s?k={query}&crid=18G82KVLYJKIC&sprefix=lapto%2Caps%2C455&ref=nb_sb_noss_2")
  assert "Amazon" in driver.title
  elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
  # print(elem.get_attribute("outerHTML"))
  # print(elem.text)
  print(f"{len(elems)} items found")
  for elem in elems:
    print(elem.text)
  time.sleep(8)
  driver.close()