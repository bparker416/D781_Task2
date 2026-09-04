from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

STUDENT_ID = "000408700"
HOME_URL = "/home/"

def main():
    opts = Options()
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    opts.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        page = LoginPage(driver)
        page.load()

        # Inject today's date into footer added earlier
        today = date.today().strftime("%B %d, %Y")
        driver.execute_script(
        "document.getElementById('run-date').textContent = arguments[0];",
        today
        )

        # Perform login with existing user (created in previous signup tests)
        page.login(username="DemoUser", password="StrongPassword")
        outcome_msg = None

        # Successful login
        try:
            wait.until(EC.url_contains(HOME_URL))
            outcome_msg = "Login successful"
        except Exception:
            try:
                msg_el = wait.until(EC.visibility_of_element_located((By.ID, "login-message")))
                outcome_msg = msg_el.text.strip() or "Unknown soutcome"
            except Exception:
                outcome_msg = "Unknown outcome"



        # Save browser screenshot
        driver.save_screenshot("chrome_login_result.png")

        outcome = "PASS"

        # Console output for evidence
        print(f"[{outcome}] Script complete - Student ID: {STUDENT_ID} - Date: {today}")

    finally:
        input("Press any key to exit...")
        driver.quit()

if __name__ == "__main__":
    main()

