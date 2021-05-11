import random
import string


def letters_lower_case(length=5, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for i in range(length))


def random_lower_string_with_numbers(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))


def letters_upper_case(length, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for i in range(length))


def random_phone(length):
    return ''.join(random.choice(string.digits) for i in range(length))


def random_number(length):
    return ''.join(random.choice(string.digits) for i in range(length))


def random_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))


def random_email_address():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(15)) + "@youtv-automation.dk"


def random_name():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(4)) + " " + ''.join(
        random.choice(string.ascii_lowercase) for i in range(4))


def random_address():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(4)) + " " + ''.join(
        random.choice(string.digits) for i in range(4))
