from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:5173/")
driver.maximize_window()

# Add task
task_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter a new task...']"))
)
task_input.send_keys("Test delete")
driver.find_element(By.XPATH, "//button[text()='Add']").click()

# Click delete icon (❌)
delete_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'delete')]"))
)
delete_button.click()

# Validate deletion
task_list = driver.find_elements(By.XPATH, "//*[contains(text(),'Test delete')]")
assert len(task_list) == 0, "❌ Task not deleted!"
print("✅ Delete Task Test Passed")

driver.quit()
