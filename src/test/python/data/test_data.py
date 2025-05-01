test_data = {
    "valid_login": {
        "username": "john",
        "password": "demo",
        "expected_result": "login_successful"
    },
    "empty_username": {
        "username": "",
        "password": "demo",
        "expected_result": "username_required"
    },
    "empty_password": {
        "username": "john",
        "password": "",
        "expected_result": "password_required"
    },
    "invalid_login": {
        "username": "JOHN",
        "password": "DEMO",
        "expected_result": "login_failed"
    },
    "forgot_login_valid_data": {
        "first_name": "Jane",
        "last_name": "Doe",
        "address": "1234 Elm St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701",
        "ssn": "123-45-6789",
        "expected_result": "redirect_to_login"
    },
    "forgot_login_missing_ssn": {
        "first_name": "Jane",
        "last_name": "Doe",
        "address": "1234 Elm St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701",
        "ssn": "",
        "expected_result": "form_error"
    },
    "forgot_login_invalid_data": {
        "first_name": "John",
        "last_name": "Smith",
        "address": "5678 Oak St",
        "city": "Hometown",
        "state": "TX",
        "zip_code": "75001",
        "ssn": "000-00-0000",
        "expected_result": "form_error"
    }
}
