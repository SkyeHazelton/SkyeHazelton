from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://selenium-python.readthedocs.io/getting-started.html")
print(driver.title)

locating = driver.find_element_by_link_text("Locating Elements")
locating.click()
driver.save_screenshot("Locating Elements Page.png")

driver.back()
driver.save_screenshot("back to homepage.png")
searchbar = driver.find_element_by_name("q")
searchbar.send_keys("xpath")
searchbar.send_keys(Keys.RETURN)
driver.save_screenshot("searched xpath.png")

driver.quit()

