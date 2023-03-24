
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.apple.com")
link = driver.current_url
baslik = driver.title
print("sayfa basliği: "+baslik)
if "apple.com" in link:
    print("Apple sayfasındayız: " + link)
driver.maximize_window()
driver.get("http://www.etsy.com")
link = driver.current_url
baslik = driver.title
print("sayfa basliği: "+baslik)
if "etsy.com" in link:
    print("Etsy sayfasındayız: "+link)
driver.back()
link = driver.current_url

#### driver.save_screenshot("./failed.png") #******CALİSMİYOR*******

if "apple.com" in link:
    print("Apple sayfasına geri döndünüz!")

#driver.close() şu anki pencereyi kapatır
#driver.quit ise selenium un kullandığı bütün pencereleri kapatır.
#yani test esnasında yeni sekmede de linkler açıldıysa bütün sekmelerin hepsini kapatır.

driver.quit()
