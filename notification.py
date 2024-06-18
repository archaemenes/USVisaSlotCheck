from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from random import randint
import os
os.chdir('/path/to/dir') # set working directory

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#chrome_options.add_argument("--no-sandbox")
# Bypass OS security model
# Initialize the webdriver with the configured options
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()
# Navigate to the webpage
driver.get("https://checkvisaslots.com/latest-us-visa-availability.html?utm_source=chr_ext")#time.sleep(2)
#visa_type_element = driver.find_element(By.CSS_SELECTOR, "span.visa_type")
#wait.until(EC.presence_of_element_located((By.ID, 'signInName')))
#visa_type_element = driver.find_element(By.XPATH, '//*[@id="last-slots"]/div[5]/div[1]/div/div[1]/div[1]/div/h3/span')
#wait = WebDriverWait(driver, 10)
visa_type_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-slots"]/div[5]/div[1]/div/div[1]/div[1]/div/h3/span')))
#driver.maximize_window()
driver.set_window_size(2010, 700)
driver.execute_script("document.body.style.zoom='90%'")
time.sleep(randint(3,6))
driver.execute_script("arguments[0].scrollIntoView(true);", visa_type_element)
time.sleep(3)
screenshot = driver.save_screenshot("./full_screenshot.png")
time.sleep(randint(1,3))
#driver.execute_script("arguments[0].scrollIntoView(true);", visa_type_element)
#visa_type_element = driver.find_element(By.TAG_NAME, "//*[contains(text(),'B1/B2 (Dropbox)')]") 
print(visa_type_element)
print("HERE")
time.sleep(5)
# Capture the screenshot
#driver.save_screenshot("./full_page_screenshot.png")
#time.sleep(randint(1,4))
driver.quit()
#//*[@id="last-slots"]/div[1]/div[1]/div/div[1]/div[1]/div/h3/span
