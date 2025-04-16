import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from data.test_data import test_data


# Test Case: Valid Login
def test_valid_login():
    data = test_data["valid_login"]
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()  # Open the login page
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    assert login_page.is_login_successful()  # Assert that login is successful
    driver.quit()

# Test Case: Invalid Login
def test_invalid_login():
    data = test_data["invalid_login"]
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()  # Open the login page
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    error_message = login_page.get_error_message()
    assert error_message == "The username and password could not be verified."  # Assert that the error message is correct
    driver.quit()

# Test Case: Empty Username
def test_empty_username():
    data = test_data["empty_username"]
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()  # Open the login page
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    error_message = login_page.get_error_message()
    assert error_message == "Please enter a username and password."  # Assert the error message for empty username
    driver.quit()

# Test Case: Empty Password
def test_empty_password():
    data = test_data["empty_password"]
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()  # Open the login page
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.submit_login()
    error_message = login_page.get_error_message()
    assert error_message == "Please enter a username and password."  # Assert the error message for empty password
    driver.quit()
