import pytest
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.login("john", "demo")
    assert login_page.is_login_successful()
    driver.quit()
