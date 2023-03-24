import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://facebook.com")
time.sleep(1)
driver.switch_to.new_window("tab")
driver.get("http://instagram.com")
time.sleep(1)
driver.switch_to.new_window("tab")
driver.get("http://twitter.com")
time.sleep(1)

def sekme_degistir(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik.lower() in driver.title.lower():
            break

sekme_degistir("facebook")
print("facebook: ", driver.title)
time.sleep(1)
sekme_degistir("instagram")
print("instagram: ", driver.title)
time.sleep(1)
sekme_degistir("twitter")
print("twitter: ", driver.title)
time.sleep(1)
driver.quit()
















