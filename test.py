import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import time
import random

def path():
    global chrome
    chrom = webdriver.Chrome()

def url_name(url):
    chrom.get(url)

    time.sleep(4)

def login(username, password):
    log_but = chrome.find_element_by_class_name("L3NKy")
    time.sleep(2)
    log_but.click()
    time.sleep(4)

    usern = chrome.find_element_by_name("username")
    usern.send_keys(username)

    passw = chrome.find_element_by_name("password")
    passw.send_keys(password)

    passw.send_keys(Keys.RETURN)
    time.sleep(5.5)

    notk = chrome.find_element_by_class_name("yWX7d")
    notk.click()
    time.sleep(3)

btc_pot = 0.0107
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
btc_price = data['bpi']['USD']['rate']
btc_price = btc_price.replace(',', '')

usd_pot = float(btc_price)*btc_pot
pot_round = round(usd_pot, 2)
first = 0.7*usd_pot
sec_reg = 0.15*usd_pot
#print("current pot: $",round(usd_pot, 2), '\n')
#print("first place: $", round(first, 2), '\n')
#print("second place and regular points: $", round (sec_reg, 2), '\n')


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
login.send_keys(username)

pass_but = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pass_but.send_keys(password)

next_but = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
next_but.click()
