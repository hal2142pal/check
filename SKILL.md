---
name: check-skill
description: "A Selenium-based skill to test the Check app. Demonstrates automated browser interaction."
metadata: {"moltbot":{"emoji":"✅","requires":{"bins":["python3","chromedriver"]},"install":[{"id":"pip","kind":"pip","packages":["selenium","webdriver-manager"],"label":"Install Selenium Dependencies"}]}}
---

# Check Skill (Selenium Test)

This skill automates the testing of the `check` application using Selenium WebDriver.

## Setup

1. Install dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Execute the skill:
   ```bash
   python3 test_selenium.py
   ```

## Functionality

The skill performs the following actions:
1. Launches a headless Chrome browser.
2. Navigates to the API documentation (`/docs`).
3. Creates a new item via JavaScript execution (`fetch`).
4. Verifies the item appears in the list (`/items/`).
