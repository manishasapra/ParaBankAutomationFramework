import pytest
from data.test_data import test_data
from pages.forgot_login_page import ForgotLoginPage

@pytest.mark.parametrize("data_key", ["forgot_login_missing_ssn", "forgot_login_invalid_data"])
def test_forgot_login_info(driver, data_key):
    data = test_data[data_key]
    forgot_login_page = ForgotLoginPage(driver)

    # Open the Forgot Login page and fill the form
    forgot_login_page.open()
    forgot_login_page.fill_form(
        first_name=data.get("first_name", ""),
        last_name=data.get("last_name", ""),
        address=data.get("address", ""),
        city=data.get("city", ""),
        state=data.get("state", ""),
        zip_code=data.get("zip_code", ""),
        ssn=data.get("ssn", "")  # Pass empty string if SSN is missing
    )
    forgot_login_page.submit()

    # Define expected error messages for each test case
    expected_errors = {
        "forgot_login_missing_ssn": "Social Security Number is required.",
        "forgot_login_invalid_data": "The customer information provided could not be found."
    }

    expected_error_message = expected_errors[data_key]
    actual_error_message = forgot_login_page.get_error_message()

    assert actual_error_message == expected_error_message, \
        f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'"
