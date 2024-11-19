from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the chrome driver
driver = webdriver.Chrome()
driver.get("https://example.com/")
h1=driver.find_element(By.XPATH, value='/html/body/div/p[2]/a')
print(h1.text)
h1.click()
