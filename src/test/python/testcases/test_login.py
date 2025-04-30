import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from data.test_data import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        login_page.logout()  # ✅ Clean up session after successful login
    else:
        error_message = login_page.get_error_message()
        expected_error = "Please enter a username and password."
        assert error_message == expected_error, f"Unexpected error message for {test_case}: {error_message}"


def test_back_button_after_logout(driver):
    data = test_data["valid_login"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()

    assert login_page.is_login_successful(), "Login failed unexpectedly."

    login_page.logout()
    driver.back()
    driver.refresh()

    # Wait for login field after refresh
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_page.username_input))
    assert login_page.is_logged_out(), "User should not be able to access dashboard after logout and back navigation."


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


