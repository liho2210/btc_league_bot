import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

btc_pot = 0.0107
password = ""
username = ""

#GET BTC DATA
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
btc_price = data['bpi']['USD']['rate']
btc_price = btc_price.replace(',', '')
usd_pot = float(btc_price)*btc_pot
pot_round = round(usd_pot, 2)
first = 0.7*usd_pot
sec_reg = 0.15*usd_pot

#GENERATE MESSAGE
message = 'GAME DAY!' + '\n' + 'Current Pot: $' + str(round(usd_pot,2)) + '\n' + 'First Place: $' + str(round(first,2)), '\n' + 'Second Place and Regular Season Leader: $' + str(round(sec_reg,2)) + '\n'

#WEB AUTOMATION
driver = webdriver.Chrome('c:\webdrivers\chromedriver.exe')
time.sleep(1)
driver.maximize_window()
driver.get('https://www.instagram.com/direct/t/340282366841710300949128331853748391396')
time.sleep(4)

#LOGIN
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name('password').send_keys(password)
time.sleep(2)

#NAVIGATE
click = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
click.click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
time.sleep(4)
driver.find_element_by_xpath("//a[@href='/direct/t/340282366841710300949128331853748391396']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

#CLOSE
driver.close()
driver.quit()

