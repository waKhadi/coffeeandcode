from sheets.reader import is_valid_email

def test_valid_email():
    assert is_valid_email("test@gmail.com") == True

def test_invalid_email_no_at():
    assert is_valid_email("testgmail.com") == False

def test_invalid_email_no_domain():
    assert is_valid_email("test@") == False

def test_invalid_email_empty():
    assert is_valid_email("") == False