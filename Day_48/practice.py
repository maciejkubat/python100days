from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_dict = {}

for index, date in enumerate(dates):
    event_dict[index] = {
        "time" : date.text,
        "name" : events[index].text
    }
print(event_dict)

driver.quit()