# React + Vite To-Do App

This project is a **To-Do application** built with **React** and **Vite**. It provides a minimal setup to get React working in Vite with **Hot Module Replacement (HMR)** and ESLint rules.

---

## Project Description

This To-Do app allows users to:

- Add new tasks  
- Edit existing tasks  
- Delete tasks  
- Mark tasks as completed  

It’s a simple, lightweight app designed to demonstrate **React component management** and **state handling**.

---

## Features

- **Add Task:** Enter a new task in the input field and click "Add".  
- **Edit Task:** Click the edit icon (✏️) on a task, update the text, and click "Update".  
- **Delete Task:** Remove tasks with the delete icon (🗑️).  
- **React + Vite:** Fast development using HMR for instant updates.  
- **ESLint Support:** Ensures clean, consistent code formatting.  

---

## Installation

1. Clone the repository:

git clone <your-repo-url>

2. Navigate to the project directory:

cd your-project-folder

3. nstall dependencies:

npm install

4. Start the development server:

npm run dev

Your app will be available at http://localhost:5173

## Usage 

Open the app in your browser.

Enter a task in the input field and click Add.

To edit a task, click the ✏️ Edit button, update the text, then click Update.

To delete a task, click the 🗑️ Delete button.

Completed tasks can be marked by clicking a checkbox (if implemented).

## Testing with Selenium

This project includes a Selenium automation script to test the Add/Edit task functionality.

Example Selenium workflow:

Add a new task.

Click the Edit button for the task.

Update the task text.

Click the Update button.

Verify the updated task appears correctly.

Python Selenium setup: pip install selenium

Sample test script:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5173/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Add task
task_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter a new task...']")))
task_input.send_keys("Cook food")
driver.find_element(By.XPATH, "//button[text()='Add']").click()
time.sleep(1)

# Edit task
edit_button_xpath = '//*[@id="root"]/div/div/div[2]/div/div/button[1]'
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))
edit_button.click()
time.sleep(1)

edit_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Cook food']")))
edit_input.clear()
edit_input.send_keys("Cook dinner")

update_button_xpath = '//*[@id="root"]/div/div/div[1]/button'
update_button = wait.until(EC.element_to_be_clickable((By.XPATH, update_button_xpath)))
update_button.click()
time.sleep(1)

# Verify updated task
task_container_xpath = '//*[@id="root"]/div/div/div[2]/div'
updated_task = wait.until(EC.presence_of_element_located((By.XPATH, task_container_xpath)))
assert "Cook dinner" in updated_task.text, "Task not edited!"
print("✅ Edit Task Test Passed")

driver.quit()
