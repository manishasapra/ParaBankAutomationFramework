from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_element_present(self.LOGOUT_LINK)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
