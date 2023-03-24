from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
seckin_madde_alani = driver.find_element(By.ID, "mp-tfa")
seckin_madde_text = seckin_madde_alani.text
seckin_madde_text = seckin_madde_text.split(",")[0]
print("seckin madde: ", seckin_madde_text)
kaliteli_madde = driver.find_element(By.ID, "mf-tfp").text
kaliteli_madde_text = kaliteli_madde.split(",")[0]
print("kaliteli madde: ", kaliteli_madde_text)
driver.quit()