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
    "locked_out_user": {
        "username": "locked_user",
        "password": "LockedPass123"
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
    },

    "register_missing_username": {
        "first_name": "John",
        "last_name": "Doe",
        "address": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701",
        "phone": "555-1234",
        "ssn": "123-45-6789",
        "username": "",
        "password": "password123",
        "confirm_password": "password123"
    },
    "register_password_mismatch": {
        "first_name": "Jane",
        "last_name": "Smith",
        "address": "456 Maple Ave",
        "city": "Shelbyville",
        "state": "IL",
        "zip_code": "62702",
        "phone": "555-5678",
        "ssn": "987-65-4321",
        "username": "janesmith",
        "password": "pass123",
        "confirm_password": "pass124"
    },
    # Existing entries...

    "register_duplicate_username": {
        "first_name": "Alex",
        "last_name": "Smith",
        "address": "456 Elm Street",
        "city": "Austin",
        "state": "TX",
        "zip_code": "73301",
        "phone": "5125550198",
        "ssn": "123-45-6789",
        "username": "existinguser123",  # Use a username that is already registered
        "password": "Test@1234",
        "confirm_password": "Test@1234"
    },

    "register_missing_ssn": {
        "first_name": "Lily",
        "last_name": "Johnson",
        "address": "789 Oak Lane",
        "city": "Dallas",
        "state": "TX",
        "zip_code": "75001",
        "phone": "2145550199",
        "ssn": "",  # SSN intentionally left blank
        "username": "lilyjohnson",
        "password": "ValidPass@1",
        "confirm_password": "ValidPass@1"
    },
    "register_missing_first_name": {
        "first_name": "",  # Leaving the first name blank
        "last_name": "Doe",
        "address": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701",
        "phone": "5551234567",
        "ssn": "123-45-6789",
        "username": "johndoe123",
        "password": "Password123!",
        "confirm_password": "Password123!"
    },
    "register_missing_password": {
        "first_name": "John",
        "last_name": "Doe",
        "address": "123 Main St",
        "city": "Metropolis",
        "state": "NY",
        "zip_code": "10001",
        "phone": "1234567890",
        "ssn": "123-45-6789",
        "username": "johndoe",
        "password": "",  # Intentionally left blank
        "confirm_password": ""
    },
    "register_missing_last_name": {
        "first_name": "Jane",
        "last_name": "",  # Intentionally blank
        "address": "123 Elm St",
        "city": "Berlin",
        "state": "Berlin",
        "zip_code": "10115",
        "phone": "0123456789",
        "ssn": "123-45-6789",
        "username": "janeuser",
        "password": "securePass123",
        "confirm_password": "securePass123"
    },"whitespace_input": {
        "username": "   ",
        "password": "   "
    }

}





