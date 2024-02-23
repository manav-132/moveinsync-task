from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://demoqa.com/login")
username_input = driver.find_element(By.ID, "userName")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login")
username_input.clear()
password_input.clear()
username_input.send_keys("manav")
password_input.send_keys("Manav12345#")
login_button.click()
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "logged-in-element")))
driver.quit()