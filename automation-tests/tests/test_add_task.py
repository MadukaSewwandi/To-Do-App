from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:5173/")
driver.maximize_window()

# Enter task
task_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter a new task...']"))
)
task_input.send_keys("Buy groceries")

# Click Add button
add_button = driver.find_element(By.XPATH, "//button[text()='Add']")
add_button.click()

# ✅ Wait for the new task to appear
added_task = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Buy groceries')]"))
)

assert "Buy groceries" in added_task.text
print("✅ Add Task Test Passed Successfully!")

driver.quit()
