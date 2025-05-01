from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://parabank.parasoft.com/parabank/index.htm"
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")
        self.logout_link = (By.LINK_TEXT, "Log Out")
        self.error_message = (By.CLASS_NAME, "error")

    def open(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.submit_login()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.logout_link))
            return self.driver.find_element(*self.logout_link).is_displayed()
        except NoSuchElementException:
            return False

    def get_error_message(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message))
            return self.driver.find_element(*self.error_message).text.strip()
        except NoSuchElementException:
            return ""

    def logout(self):
        try:
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.logout_link)
            )
            logout_button.click()
        except TimeoutException:
            raise Exception("Logout link not found or not clickable.")

    def is_logged_out(self):
        try:
        # Check if the username input is visible, indicating that the login page is shown
            return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.username_input)
        ).is_displayed()
        except TimeoutException:
            return False

