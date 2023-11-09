from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions
import time
import json

driver = webdriver.Chrome()  # You'll need to download the appropriate driver for your browser

with open("link.txt", 'r') as file:
    link = file.read().strip()
driver.get(link)
time.sleep(2)

try:
	cookies = driver.find_element("id", "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
	cookies.click()
	time.sleep(2)
except NoSuchElementException:
	pass

try:
	close_button = driver.find_element(By.XPATH, '//button[contains(span/text(), "Close")]')
	close_button.click()
	time.sleep(2)
except NoSuchElementException:
	pass

with open("output.json", 'r') as file:
    songlist = json.load(file)

errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=30, poll_frequency=1, ignored_exceptions=errors)
submitButtonSelector = '//button[span[text()="Submit "]]'
goBackButtonSelector = './/button[contains(span/text(), "Go Back")]'

for item in songlist:

	input_name_field = driver.find_element("id", "username")
	input_name_field.send_keys(Keys.CONTROL + "a")
	input_name_field.send_keys(Keys.DELETE)
	input_name_field.send_keys(item["name"])

	input_song_field = driver.find_element("id", "submitSong")
	input_song_field.send_keys(item["link"])
	
	wait.until(expected_conditions.element_to_be_clickable((By.XPATH, submitButtonSelector))).click()

	wait.until(expected_conditions.visibility_of_element_located((By.XPATH, goBackButtonSelector))).click()
	
	time.sleep(2)

# Close the browser
driver.quit()