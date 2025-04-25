import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from data.test_data import test_data


@pytest.fixture
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_valid_login(driver):
    data = test_data["valid_login"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    assert login_page.is_login_successful(), "Login should be successful with valid credentials"


def test_invalid_login(driver):
    data = test_data["invalid_login"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    time.sleep(3)  # TEMP: let error show
    error_message = login_page.get_error_message()
    assert error_message in [
        "The username and password could not be verified.",
        "Internal Server Error"
    ], f"Unexpected error message: {error_message}"


def test_empty_username(driver):
    data = test_data["empty_username"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    error_message = login_page.get_error_message()
    assert error_message == "Please enter a username and password.", f"Expected error for empty username. Got: {error_message}"


def test_empty_password(driver):
    data = test_data["empty_password"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    error_message = login_page.get_error_message()
    assert error_message == "Please enter a username and password.", f"Expected error for empty password. Got: {error_message}"
