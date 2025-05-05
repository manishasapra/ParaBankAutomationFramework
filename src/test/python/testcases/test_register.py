import pytest
from data.test_data import test_data
from pages.register_page import RegisterPage

@pytest.mark.parametrize("data_key", [
    "register_missing_username",
    "register_password_mismatch",
    "register_missing_ssn",
    "register_missing_first_name"
])
def test_register_form_validation(driver, data_key):
    data = test_data[data_key]
    register_page = RegisterPage(driver)

    # Navigate to the Register page and fill the form
    register_page.open()
    register_page.fill_form(
        first_name=data.get("first_name", ""),
        last_name=data.get("last_name", ""),
        address=data.get("address", ""),
        city=data.get("city", ""),
        state=data.get("state", ""),
        zip_code=data.get("zip_code", ""),
        phone=data.get("phone", ""),
        ssn=data.get("ssn", ""),
        username=data.get("username", ""),
        password=data.get("password", ""),
        confirm_password=data.get("confirm_password", "")
    )
    register_page.submit()

    # Define expected error messages for validation cases
    expected_errors = {
        "register_missing_username": "Username is required.",
        "register_password_mismatch": "Passwords did not match.",
        "register_missing_ssn": "Social Security Number is required.",
        "register_missing_first_name": "First name is required."
    }

    if data_key in expected_errors:
        expected_error_message = expected_errors[data_key]
        actual_error_message = register_page.get_error_message()
        assert actual_error_message == expected_error_message, \
            f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'"
