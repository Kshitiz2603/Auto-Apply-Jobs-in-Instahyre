from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

# Set up ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"  # Update with your actual path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Instahyre login page
driver.get("https://www.instahyre.com/login/")

# Wait for the page to load
time.sleep(3)

# Enter email
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("EMAIL")  # Replace with your email

# Enter password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("PASSWORD")  # Replace with your password

# Press Enter to login or click the Login button
password_field.send_keys(Keys.RETURN)

# # Wait for login to complete
time.sleep(10)

jobSearch_field = driver.find_element(By.ID, "job-search-section")
jobSearch_field.click() 

# Wait for the page to load
time.sleep(10)

showresult_field = driver.find_element(By.ID, "show-results")
showresult_field.click() 

# Wait for the page to load
time.sleep(10)

# Click "View" button for a job 
view_button = driver.find_element(By.ID, "interested-btn")
view_button.click()

# Wait for the apply button to appear
time.sleep(2)

jobsApplied = 0

while True:
    try:
        # Find and click the "Apply" button
        apply_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.new-btn")
        apply_button.click()
        jobsApplied += 1
        print("Clicked Apply button")

        # Wait before clicking again (adjust delay as needed)
        time.sleep(2)

    except Exception as e:
        print("Error clicking apply button:", e)
        break  


print(f"Total jobs applied: {jobsApplied}")


# Wait and then close browser
time.sleep(3)
driver.quit()
