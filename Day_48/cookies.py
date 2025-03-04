from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading
import sys
INTERVAL = 30

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def timeout():
    cps = driver.find_element(By.CSS_SELECTOR, value="#cps")
    print(cps)
    sys.exit(0)

timer = threading.Timer(300, timeout)  # Set timer for 5 seconds
timer.start()

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

current_time = time.time()
current_seconds = int(current_time) % 60
second_clicked = current_seconds
while True:
    current_time = time.time()
    current_seconds = int(current_time) % 60
    lowest_price = 0
    if current_seconds % INTERVAL == 0 and second_clicked != current_seconds:
        second_clicked = current_seconds
        money = driver.find_element(By.CSS_SELECTOR, "#money")
        print(f"{current_seconds} seconds is divisible by {INTERVAL}. Money: {money.text}")
        money_int = int(money.text.replace(",", ""))
        store_items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        for index,item in enumerate(store_items):
            item_text = item.text
            print(item_text)
            item_text = item_text.replace(",","")
            try:
                item_price = int(item_text.split(' - ')[1])
                print(f"{item_price}")
                if money_int > item_price > lowest_price:
                    lowest_price = item_price
                else:
                    try:
                        store_items[index-1].click()
                        lowest_price = 0
                        break
                    except Exception as e:
                        break
            except IndexError:
                pass
    cookie.click()