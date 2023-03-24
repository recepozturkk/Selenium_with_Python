import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://ucuzabilet.com")
# //li[contains(text(), 'VIE')]

input = driver.find_element(By.ID, "from_text")
input.send_keys("avust")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 150)", "")
time.sleep(2)
graz = driver.find_element(By.XPATH, "//li[contains(text(), 'GRZ')]")
graz.click()

time.sleep(2)
driver.quit()
