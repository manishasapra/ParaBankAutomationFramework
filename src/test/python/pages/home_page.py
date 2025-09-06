from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://parabank.parasoft.com/parabank/index.htm"

        # Locators
        self.logo = (By.XPATH, "//img[@alt='ParaBank']")
        self.home_link = (By.LINK_TEXT, "Home")
        self.products_link = (By.LINK_TEXT, "Products")
        self.locations_link = (By.LINK_TEXT, "Locations")
        self.about_us_link = (By.LINK_TEXT, "About Us")
        self.services_link = (By.LINK_TEXT, "Services")
        self.solutions_link = (By.LINK_TEXT, "Solutions")

    def open(self):
        self.driver.get(self.url)

    def click_home(self):
        self.click(self.home_link)

    def click_products(self):
        self.click(self.products_link)

    def click_locations(self):
        self.click(self.locations_link)

    def click_about_us(self):
        self.click(self.about_us_link)

    def click_services(self):
        self.click(self.services_link)

    def click_solutions(self):
        self.click(self.solutions_link)

    def is_logo_displayed(self):
        return self.is_element_present(self.logo)

    def click_contact(self):
        self.driver.find_element(By.LINK_TEXT, "Contact Us").click()