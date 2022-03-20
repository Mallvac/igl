from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
opt = Options()
opt.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.instagram.com/p/CbSeHMaOaTP/")
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
print("As of twime I can't gwet my app authowised, so you gotta login into youw facebook accowount. Sowwy :(")
email = input("Usew Email:")
password = input("Usew Passwowd:")

time.sleep(100)
