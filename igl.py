#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys
import msvcrt
import time

#thanks to https://stackoverflow.com/users/9939262/sagar I can't be bothered to do this shit
def password_input(prompt=''):
    p_s = ''
    proxy_string = [' '] * 64
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\r':
            break
        elif c == b'\x08':
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = "*"
            p_s += c.decode()
    sys.stdout.write('\n')
    return p_s

def login():
    email = input("Usew Email:")
    password = password_input("User Passwowd:")
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    #If I overwrite password and email in RAM this means it's safe, right ?
    email = 0
    password = 0
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    #Check if user was logged into thiers account
    try:
        check = True
        driver.find_element(By.XPATH, '//*[@id="slfErrorAlert"]')
    except:
        print("One time session login sucessful !")
        check = False
    if check:
        login()

# Webdriver Inits and stuff
opt = Options()
opt.add_argument("--headless")
#,options=opt
driver = webdriver.Chrome("chromedriver.exe")

#Accept cookies or smthng, idk I'm not a lawyer
driver.get("https://www.instagram.com/p/CbSeHMaOaTP/")
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
print("As of twime I can't gwet my app authowised, so you gotta login into youw facebook accowount. Sowwy :(")
#Start Login loppty doopty
login()

driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()


time.sleep(100)
