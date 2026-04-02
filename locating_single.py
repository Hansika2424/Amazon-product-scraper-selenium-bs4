from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=18G82KVLYJKIC&sprefix=lapto%2Caps%2C455&ref=nb_sb_noss_2")
assert "Amazon" in driver.title
elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.get_attribute("outerHTML"))
time.sleep(8)
driver.close()
# elem.clear()
# elem.send_keys("pyco n")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(10)
# driver.close()