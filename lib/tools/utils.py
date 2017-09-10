from rest_framework.test import APIClient, APITestCase

from lib.companies.create import (
    create_company
)
# import payload_generator
from lib.tools.payload_generator import (
    generate_company_data,
)
from lib.users.create import create_user


def create_random_company(user_id):
    company_data = generate_company_data(
        creator_id=user_id
    )
    company = create_company(**company_data)
    return company


class UserFactory:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.user = create_user(self.username, self.password, self.email)

    @property
    def client(self):
        client = APIClient(enforce_csrf_checks=False)
        return client


class BaseTestCase(APITestCase):
    def setUp(self):
        # create user
        self.password = 123
        self.anonymous_client = APIClient(enforce_csrf_checks=True)
        self.users = {
            'admin': UserFactory('admin', self.password, 'admin@example.com'),
            'member': UserFactory('member', self.password,
                                  'member@example.com'),
            'recruiter': UserFactory('recruiter', self.password,
                                     'recuiter@example.com'),
            'stranger': UserFactory('stranger', self.password,
                                    'stranger@example.com')
        }

        # create companies
        company1 = create_random_company(user_id=self.users['admin'].user.id)
        company2 = create_random_company(user_id=self.users['admin'].user.id)
        self.companies = [company1, company2]
