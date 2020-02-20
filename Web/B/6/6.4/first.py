class InvalidEmail(Exception):
    """
    Used to identify invalid email addresses
    """
    pass


class MissingAt(InvalidEmail):
    """
    Used to identify the absence of the @ symbol email address
    """
    pass


class MissingDomainDot(InvalidEmail):
    """
    Used to identify the absence of a dot in the domain part of the email address
    """
    pass


class InvalidArgumentType(InvalidEmail):
    pass


def valid_email(email):
    """
    Checks for at least one dot in the domain and the @ sign in the email.
    Returns True if email is valid, otherwise throws an InvalidEmail exception
    """
    assert isinstance(email, str), "Input waiting for a string (str)"
    parts = email.split("@")
    if not isinstance(email, str):
        raise InvalidArgumentType("Invalid type, expected string")
    if len(parts) != 2:
        raise MissingAt("Missing @ symbol")
    address, domain = parts
    if "." not in domain:
        raise MissingDomainDot("Missing point in the domain part")
    return True


emails = []
for x in range(3):
    address = input("Enter your email: ")
    emails.append(address)
try:
    valid = valid_email(emails)
except AssertionError:
    print("Incorrect variable name")
except MissingAt:
    print("There is no @ symbol")
except MissingDomainDot:
    print("There is no point symbol")
