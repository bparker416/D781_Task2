from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.signup_page import SignupPage

STUDENT_ID = "000408700"

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        page = SignupPage(driver)
        page.load()

        # Inject today's date
        today_str = date.today().strftime("%B %d, %Y")
        driver.execute_script(
            "document.getElementById('run-date').textContent = arguments[0];",
            today_str
        )

        # Create unique username with timestamp to avoid duplicate user errors
        timestamp = datetime.now().strftime("%H%M%S")
        unique_username = f"DemoUser{timestamp}"

        # Fill and submit sign-up form
        page.fill_form(
            username=unique_username,
            email=f"demo{timestamp}@demo.email",
            password="StrongPassword"
        )
        page.submit()

        outcome = "PASS" if page.succeeded() else "FAIL"

        # Capture evidence
        driver.save_screenshot("chrome_signup_result.png")

        # Console output required by the rubric
        print(
            f"[{outcome}] Script completed - Student ID: {STUDENT_ID} - Date: {today_str}"
        )
        print(f"Created user: {unique_username}")

    finally:
        input("Press any key to exit...")
        driver.quit()

if __name__ == "__main__":
    main()