from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.uitestingplayground.com/ajax")

findField = driver.find_element(By.ID, 'ajaxButton')
findField.click()
driver.implicitly_wait(20)
findField = driver.find_element(By.CLASS_NAME, 'bg-success')



# driver.close()