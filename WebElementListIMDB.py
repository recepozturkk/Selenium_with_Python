import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.imdb.com/")
driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']"  ).click()
film_list = driver.find_elements(By.XPATH,"//table/tbody//tr//td[@class='titleColumn']")

for i in film_list:
    if int(i.text[-5:-1])>= 2000:
        print(i.text)



driver.quit()