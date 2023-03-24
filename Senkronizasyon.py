import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#driver.implicitly_wait(30)
# driver nesnesi driver.quit ile süreç bitmediği bütün driver işlemlerinde 20sn bekleyecek.
driver.get("https://pynishant.github.io/Selenium-python-waits.html")

tryit = driver.find_element(By.XPATH,"//button[contains(text(), 'Try it')]").click()
# webdriverwait ile explicit wait oluşturulur ve tek sefer çalışır sonraki kodlarda çalışmaz.
WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located((By.ID, "waitCreate")))
clickme = driver.find_element(By.ID,"waitCreate").click()
WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())

uyari = Alert(driver)
time.sleep(1)
uyari.accept()
driver.quit()

#implicit wait-gizli bekleme
#explicit wait-açıktan bekleme
#fluent wait- explicit wait in içine parametre vererek çalıştırılması


