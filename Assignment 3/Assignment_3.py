# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigating to the Canadian tire homepage
driver.get("https://www.canadiantire.ca/en.html")
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("xpath", "/html/body/div[1]/div/div/div/header/div/div/div/div[3]/div[2]/div/div/div[2]/div[1]/span/div/div/div[2]/div[2]/div[1]/input")
search_bar.send_keys("bicycle")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(3)

# Selecting a bicycle from the search results
bicycle_link_1 = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[5]/div[2]/div/div[1]/span/div/div[3]/div/ul/li[1]/a/div/div/div[1]")
bicycle_link_1.click()

# Waiting for the bicycle details page to load
time.sleep(3)

# Adding the bicycle to the cart
add_to_cart_button = driver.find_element("id", "add-to-cart")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on continue button
continue_button = driver.find_element("id", "continue-btn")
continue_button.click()
time.sleep(3)

# selecting another bicycle
bicycle_link_2 = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[9]/div/div/span/div/div/div[2]/div/div/div/div/div[6]/div/a/div/div/div[1]/img")
bicycle_link_2.click()

time.sleep(3)

# Adding the bicycle to the cart
add_to_cart_button = driver.find_element("id", "add-to-cart")
add_to_cart_button.click()
time.sleep(5)

# selecting lock cable
lock_cable_link = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[29]/span/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/a")
lock_cable_link.click()
time.sleep(3)

# Adding lock cable to cart
add_to_cart_button = driver.find_element("id", "add-to-cart")
add_to_cart_button.click()
time.sleep(5)

# Continue to cart
cart = driver.find_element("id", "footer-btn")
cart.click()
time.sleep(5)

# Removing item
remove_lock_cable_link = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div[4]/span/div/div/div/div/div/div[2]/div/div/div/div/div[4]/button[2]/span")
remove_lock_cable_link.click()
time.sleep(5)

# proceed_to_checkout
checkout_items = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[3]/div/div[1]/div[2]/div/div/span/div/div/div[4]/button")
checkout_items.click()

time.sleep(5)

# Closing the webdriver
driver.close()
