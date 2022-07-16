from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://demo.anhtester.com/basic-first-form-demo.html')
driver.implicitly_wait(5)
try:
    ad = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    ad.click()
except:
    print('No element with this class name. Skipping...')

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')
btn_clc_sum = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')

sum1_entered = 12
sum2_entered = 15
sum1.send_keys(sum1_entered)
sum2.send_keys(sum2_entered)
btn_clc_sum.click()
result = int(driver.find_element(By.ID, 'displayvalue').text)
if(sum1_entered + sum2_entered) == result:
    print('Sum calculator works properly')
else:
    print('Fix the sum calculator')