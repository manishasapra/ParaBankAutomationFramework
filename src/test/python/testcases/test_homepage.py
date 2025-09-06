

import pytest
from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_homepage_logo(driver):
    home = HomePage(driver)
    home.open()
    assert home.is_logo_displayed(), "Logo is not displayed on homepage"

def test_home_link(driver):
    home = HomePage(driver)
    home.open()
    home.click_home()
    assert "ParaBank" in driver.title

def test_products_link(driver):
    home = HomePage(driver)
    home.open()
    home.click_products()
    assert "Products" in driver.page_source

def test_locations_link(driver):
    home = HomePage(driver)
    home.open()
    home.click_locations()
    assert "location" in driver.page_source.lower()

def test_about_us_link(driver):
    home = HomePage(driver)
    home.open()
    home.click_about_us()
    assert "About Us" in driver.page_source

def test_services_link(driver):
    home = HomePage(driver)
    home.open()
    home.click_services()
    assert "Services" in driver.page_source

def test_contact_link(driver):
    home = HomePage(driver)
    home.open()
    home.click_contact()
    assert "Customer Care" in driver.page_source or "Contact Us" in driver.page_source
