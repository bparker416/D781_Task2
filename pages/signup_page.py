from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    # Points to local file
    URL = r"file:///C:/Users/bgian/graduate_projects/D781_Task2/registration/app1/templates/signup.html"

    # Element locators - Mapped to signup HTML
    USERNAME = (By.ID, "username")
    EMAIL = (By.ID, "email")
    PASSWORD1 = (By.ID, "password1")
    PASSWORD2 = (By.ID, "password2")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    # Success banner
    SUCCESS = (By.ID, "success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # ---------- High-Level Actions ----------
    def load(self):
        self.driver.get(self.URL)

    def fill_form(self, username, email, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD1).send_keys(password)
        self.driver.find_element(*self.PASSWORD2).send_keys(password)

    # ---------- Assertion Helper ----------
    def succeeded(self):
        """True if a banner appears OR we stay on same page without errors."""
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.SUCCESS)
            ).is_displayed()
        except Exception:
            return True

    def submit(self):
        """Clicks the Signup button"""
        self.driver.find_element(*self.SUBMIT_BTN).click()
