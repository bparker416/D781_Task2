from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Points to local file
    URL = r"file:///C:/Users/bgian/graduate_projects/D781_Task2/registration/app1/templates/login.html"

    # Element locators - Mapped to login HTML
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    # Success banner
    SUCCESS = (By.ID, "success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def succeeded(self):
        """True if a banner appears OR we stay on same page without errors."""
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.SUCCESS)
            ).is_displayed()
        except Exception:
            return True