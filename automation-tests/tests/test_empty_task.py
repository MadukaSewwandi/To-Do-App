from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:5173/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[text()='Add']").click()

# Ensure no <li> is added
tasks = driver.find_elements(By.TAG_NAME, "li")
assert len(tasks) == 0, "❌ Empty task was added!"
print("✅ Empty Task Validation Test Passed")

driver.quit()
