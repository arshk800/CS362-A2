def check_pwd(password):
    """Function checks password requirements"""
    length = len(password)
    symbols = "~`!@#$%^&*()_+-="

    # If length less than 8 or greater than 20
    if length < 8 or length > 20:
        return False

    # If none of the chars are lower
    if not any(i.islower() for i in password):
        return False

    # If none of the chars are upper
    if not any(i.isupper() for i in password):
        return False

    # If none of the chars are a digit
    if not any(i.isdigit() for i in password):
        return False

    # If none of the chars are a symbol
    if not any(i in symbols for i in password):
        return False

    # else return True
    return True




