

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
        "expected_result": "login_successful"
    }
}