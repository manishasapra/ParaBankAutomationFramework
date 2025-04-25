

test_data = {
    "valid_login": {
        "username": "john",
        "password": "demo",
        "expected_result": "login_successful"
    },
    "invalid_login": {
        "username": "invalid_user",
        "password": "invalid_pass",
        "expected_result": "invalid_credentials"
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
    }
}
