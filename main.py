from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://demo.anhtester.com/jquery-download-progress-bar-demo.html')
myElement = driver.find_element(By.ID, "downloadButton")
myElement.click()