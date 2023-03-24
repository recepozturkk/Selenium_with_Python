import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://apple.com")
time.sleep(1)
print(driver.title)
apple = driver.current_window_handle
driver.switch_to.new_window("tab")
driver.get("https://tesla.com")
time.sleep(1)
print(driver.title)
tesla = driver.current_window_handle
driver.switch_to.window(apple)
print(driver.title)
time.sleep(1)
driver.switch_to.window(tesla)
print(driver.title)
time.sleep(1)
driver.switch_to.window(apple)
print(driver.title)
time.sleep(1)




driver.quit()