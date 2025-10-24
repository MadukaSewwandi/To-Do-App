from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5173/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# =========================
# 1️⃣ Add a new task
# =========================
task_name = "Cook food"
task_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter a new task...']"))
)
task_input.send_keys(task_name)
driver.find_element(By.XPATH, "//button[text()='Add']").click()
time.sleep(1)  # Wait for task to appear

# =========================
# 2️⃣ Click the Edit button for the added task
# =========================
edit_button_xpath = '//*[@id="root"]/div/div/div[2]/div/div/button[1]'
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))
edit_button.click()
time.sleep(1)  # Wait for edit input to appear

# =========================
# 3️⃣ Edit the task
# =========================
edit_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@value='Cook food']"))
)
updated_task_name = "Cook dinner"
edit_input.clear()
edit_input.send_keys(updated_task_name)

# =========================
# 4️⃣ Click the Update button
# =========================
update_button_xpath = '//*[@id="root"]/div/div/div[1]/button'
update_button = wait.until(EC.element_to_be_clickable((By.XPATH, update_button_xpath)))
update_button.click()
time.sleep(1)

# =========================
# 5️⃣ Verify the updated task
# =========================
task_container_xpath = '//*[@id="root"]/div/div/div[2]/div'
updated_task = wait.until(EC.presence_of_element_located((By.XPATH, task_container_xpath)))
assert updated_task_name in updated_task.text, "Task not edited!"
print("✅ Edit Task Test Passed")

driver.quit()
