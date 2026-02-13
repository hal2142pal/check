from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup
os.makedirs("docs", exist_ok=True)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=800,600")

driver = webdriver.Chrome(options=chrome_options)

try:
    print("Navigating to app...")
    driver.get("http://127.0.0.1:8000")
    
    # Wait for app to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    time.sleep(1) # Extra buffer for render

    # 1. Initial State
    print("Capturing home.png")
    driver.save_screenshot("docs/home.png")

    # 2. Add Task
    print("Adding task...")
    input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    input_box.send_keys("Buy milk")
    input_box.send_keys(Keys.RETURN)
    
    # Wait for item to appear
    time.sleep(1) 
    print("Capturing added.png")
    driver.save_screenshot("docs/added.png")

    # 3. Complete Task
    print("Completing task...")
    checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox.click()
    
    time.sleep(1)
    print("Capturing completed.png")
    driver.save_screenshot("docs/completed.png")

except Exception as e:
    print(f"Error: {e}")
    # Capture error screenshot
    driver.save_screenshot("docs/error.png")

finally:
    driver.quit()
    print("Done.")
