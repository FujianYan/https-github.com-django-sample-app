import random
import string

CHARS = (
    string.ascii_uppercase + string.ascii_lowercase + string.digits
)


def random_string(length=10, chars=CHARS):
    """
    Generate a random alphanumeric string of the specified length.
    """
    return str(''.join(random.choice(chars) for _ in range(length)))


def random_integer():
    """
    Generate a random integer of the specified length.
    """
    return random.randint(1, 10000)


def generate_company_data(**data):
    """
    Generate payload data for company api
    """
    company_data = {
        'creator_id': data.get('creator_id'),
        'company_name': data.get('company_name', random_string())
    }
    return company_data
