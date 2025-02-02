from datetime import date
import re

def validate_name(value: str) -> str:
    """Validate that a name is at least 2 characters long and return a formatted name."""
    if len(value.strip()) < 2:
        raise ValueError('Name must be greater than one character!')
    if value.isspace():
        raise ValueError("Name cannot be whitespace!")
    if  any(char.isdigit() for char in value):
        raise ValueError("Name cannot contain a digit!")
    return value.title().strip()


def validate_phone(value: str) -> str:
    """
    Validate that a phone number contains exactly 10 -11 digits and an optional
    '+' with a 2- digit country code.
    """
    phone_pattern = re.compile(r"^(?:\+?\d{2})?\d{10,11}$")
    if not phone_pattern.match(value.strip()):
        raise ValueError("Invalid phone number format")
    return value

def student_id(value: str) -> str:
    pattern = r'^(?i)STU/(\d{2})/(\d{2})/([0-9]{4})$'
    match = re.match(value, pattern)
    if not match:
        raise Exception
    first_num = int(match.group(1))
    second_num = int(match.group(2))

    if second_num != first_num + 1:
        raise Exception
    return value.upper()




