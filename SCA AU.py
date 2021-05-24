

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

#go to SCA AU website
driver.get("https://www.supercheapauto.com.au/")
print(driver.title)

# At bottom of page, click on Gift Cards (linktext) - or type gift card into the search bar
link = driver.find_element_by_link_text("Gift Cards")
link.click()

# Click on check balance - ie, click a button
button = driver.find_element_by_partial_link_text("Check Balance")
button.click()

#try:
#    element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Check My Balance"))
#    )
#    element.click()

#except:
#    driver.quit()



#type in the gift card number - auto fill the gift card number

#click on check balance without a pin

# auto fill in the wrong pin

#clear the pin

#auto fill in the correct pin

# select check balance

