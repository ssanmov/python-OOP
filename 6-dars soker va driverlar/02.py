from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
assert "Google" in driver.title
searchbar = driver.find_element(by="name", value="q")
searchbar.clear()
searchbar.send_keys("Programming")
searchbar.send_keys(Keys.RETURN)