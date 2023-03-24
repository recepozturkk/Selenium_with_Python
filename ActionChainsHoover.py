import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/hovers")

user = driver.find_element(By.CSS_SELECTOR, "div.figure")
username = driver.find_element(By.CSS_SELECTOR, "div.figcaption h5")
link = driver.find_element(By.CSS_SELECTOR, "div.figcaption a")
print(username.is_displayed())
print("isim", username.text)
time.sleep(2)

hoover = ActionChains(driver)
hoover.move_to_element(user)
hoover.perform()
time.sleep(2)
print("---------------")
print(user.is_displayed())
print("isim", username.text)
link.click()
time.sleep(2)
url = driver.current_url
assert "users/1" in url
driver.quit()