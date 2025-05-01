from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ForgotLoginPage:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get("https://parabank.parasoft.com/parabank/lookup.htm")

    def fill_form(self, first_name, last_name, address, city, state, zip_code, ssn):
        self.driver.find_element(By.NAME, "firstName").send_keys(first_name)
        self.driver.find_element(By.NAME, "lastName").send_keys(last_name)
        self.driver.find_element(By.NAME, "address.street").send_keys(address)
        self.driver.find_element(By.NAME, "address.city").send_keys(city)
        self.driver.find_element(By.NAME, "address.state").send_keys(state)
        self.driver.find_element(By.NAME, "address.zipCode").send_keys(zip_code)
        self.driver.find_element(By.NAME, "ssn").send_keys(ssn)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Find My Login Info']").click()

    def get_retrieved_username(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "lookupResponse"))
            )
            return element.text
        except TimeoutException:
            return None
    def get_error_message(self):
        try:
            # Check for SSN-specific error
            return self.driver.find_element(By.ID, "ssn.errors").text
        except NoSuchElementException:
            try:
                # Check for general error message
                return self.driver.find_element(By.CSS_SELECTOR, "p.error").text
            except NoSuchElementException:
                return None


