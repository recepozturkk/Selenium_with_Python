from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/login")
# usernameButton = driver.find_element(By.ID, "username")
# usernameButton.click()
# usernameButton.send_keys("tomsmith")
# passwordButton = driver.find_element(By.ID, "password")
# passwordButton.click()
# passwordButton.send_keys("SuperSecretPassword!")
# driver.find_element(By.CLASS_NAME, "radius").click()
# link = driver.current_url
# if "secure" in link:
#     print("Login test is successful with correct crediantials :-)")
# else:
#     print("Login test is failed with correct crediantials:-(")
# #### If username is incorrect
# driver.get("https://the-internet.herokuapp.com/login")
# usernameButton = driver.find_element(By.ID, "username")
# usernameButton.click()
# usernameButton.send_keys("recep")
# passwordButton = driver.find_element(By.ID, "password")
# passwordButton.click()
# passwordButton.send_keys("SuperSecretPassword!")
# driver.find_element(By.CLASS_NAME, "radius").click()
# link = driver.current_url
# if "secure" in link:
#     print("Login test is failed ")
# else:
#     print("Login test is successful ")
# #### If password is incorrect
# driver.get("https://the-internet.herokuapp.com/login")
# usernameButton = driver.find_element(By.ID, "username")
# usernameButton.click()
# usernameButton.send_keys("tomsmith")
# passwordButton = driver.find_element(By.ID, "password")
# passwordButton.click()
# passwordButton.send_keys("asad156165")
# driver.find_element(By.CLASS_NAME, "radius").click()
# link = driver.current_url
# if "secure" in link:
#     print("Login test is failed ")
# else:
#     print("Login test is successful ")
# #### If both is incorrect
# driver.get("https://the-internet.herokuapp.com/login")
# usernameButton = driver.find_element(By.ID, "username")
# usernameButton.click()
# usernameButton.send_keys("recep")
# passwordButton = driver.find_element(By.ID, "password")
# passwordButton.click()
# passwordButton.send_keys("asad156165")
# driver.find_element(By.CLASS_NAME, "radius").click()
# link = driver.current_url
# if "secure" in link:
#     print("Login test is failed ")
# else:
#     print("Login test is successful ")
# driver.quit()

def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "radius").click()
    message = driver.find_element(By.ID,"flash").text
    return message

message = login("tomsmith","SuperSecretPassword!")

if "secure" in message:
    print("TEST BASARILI! Doğru girdilerle login gerçekleştirildi. ")
else:
    print("TEST BAŞARISIZ! Doğru girdilerle login gerçekleştirilemedi.")

message = login("recep", "SuperSecretPassword!")
if "secure" not in message:
    print("TEST BAŞARILI ")
else:
    print("TEST BAŞARISIZ")

message = login("tomsmith", "afkak123")
if "secure" not in message:
    print("TEST BAŞARILI ")
else:
    print("TEST BAŞARISIZ ")

message = login("recep","afhap132")
if "secure" not in message:
    print("TEST BAŞARILI ")
else:
    print("TEST BAŞARISIZ ")

driver.quit()