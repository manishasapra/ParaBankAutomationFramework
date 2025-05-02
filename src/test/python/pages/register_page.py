from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://parabank.parasoft.com/parabank/register.htm"
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, first_name, last_name, address, city, state,
                  zip_code, phone, ssn, username, password, confirm_password):
        self.driver.find_element(By.ID, "customer.firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "customer.lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "customer.address.street").send_keys(address)
        self.driver.find_element(By.ID, "customer.address.city").send_keys(city)
        self.driver.find_element(By.ID, "customer.address.state").send_keys(state)
        self.driver.find_element(By.ID, "customer.address.zipCode").send_keys(zip_code)
        self.driver.find_element(By.ID, "customer.phoneNumber").send_keys(phone)
        self.driver.find_element(By.ID, "customer.ssn").send_keys(ssn)
        self.driver.find_element(By.ID, "customer.username").send_keys(username)
        self.driver.find_element(By.ID, "customer.password").send_keys(password)
        self.driver.find_element(By.ID, "repeatedPassword").send_keys(confirm_password)

    def submit(self):
        self.driver.find_element(By.XPATH, "//input[@value='Register']").click()

    def get_error_message(self):
        try:
            # Try <span class="error"> or <p class="error"> — both are used on the site
            error_element = self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, "//span[@class='error'] | //p[@class='error']"
                ))
            )
            return error_element.text.strip()
        except:
            return None
