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


@pytest.mark.parametrize("test_case", ["valid_login", "empty_username", "empty_password"])
def test_login(driver, test_case):
    data = test_data[test_case]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()

    if test_case == "valid_login":
        assert login_page.is_login_successful(), "Login should be successful with valid credentials."
    else:
        error_message = login_page.get_error_message()
        expected_error = "Please enter a username and password."
        assert error_message == expected_error, f"Unexpected error message for {test_case}: {error_message}"

def test_invalid_login(driver):
    data = test_data["invalid_login"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()

    # Wait for and check the error message instead of is_login_successful
    error_message = login_page.get_error_message()
    assert error_message == "The username and password could not be verified.", f"Unexpected error message: {error_message}"

