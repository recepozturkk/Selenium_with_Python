from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver.exe")
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-infobars")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-notifications")
options.add_argument("--disable-save-password")
options.add_argument("--disable-extensions")
options.add_argument("download.default_directory=C:/kullanicilar/ali/test")
options.add_argument("--window-size=768,1024")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(service=service, options=options)


