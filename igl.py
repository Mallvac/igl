from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
opt = Options()
opt.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.instagram.com/p/CbSeHMaOaTP/")
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
print("As of time I can't get my app authorised, so you gotta login into your facebook account. Sorry :(")
email = input("User Email:")
password = input("User Password:")

time.sleep(100)
