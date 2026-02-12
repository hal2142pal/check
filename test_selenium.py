from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

def test_checklist_app():
    print("Starting Selenium Test...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        # Use webdriver_manager to install/locate chromedriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"Failed to initialize Chrome Driver: {e}")
        # Fallback or exit if driver fails
        sys.exit(1)
    
    try:
        # Navigate to the app
        driver.get("http://localhost:8000/docs")
        print("Accessed API documentation successfully.")

        # Test creating an item via API (using execute_script for fetch)
        driver.execute_script("""
            fetch('http://localhost:8000/items/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title: 'Test Item from Selenium'
                })
            });
        """)
        time.sleep(2)
        print("Created item via fetch.")

        # Verify item exists
        driver.get("http://localhost:8000/items/")
        page_source = driver.page_source
        if "Test Item from Selenium" in page_source:
            print("Verification Successful: Item found in list.")
        else:
            print("Verification Failed: Item not found.")
            print(f"Page Source: {page_source}")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_checklist_app()
