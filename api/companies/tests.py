import json

from rest_framework import status

from lib.tools.payload_generator import random_string
from lib.tools.utils import BaseTestCase, create_random_company


class CompanyListAPIViewTestCase(BaseTestCase):
    def setUp(self):
        super(CompanyListAPIViewTestCase, self).setUp()
        self.url = '/api/companies/'

    def test_get_company_list(self):
        """
        GET /api/companies success
        """
        response = self.users['admin'].client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        companies = json.loads(response.content)

        # check number of company
        self.assertEqual(len(companies), 2)

    def test_post_company(self):
        """
        POST /api/companies/ success
        """
        # post company
        company_name = random_string()
        self.data = {'company_name': company_name,
                     'creator_id': self.users['admin'].user.id}
        response = self.users['admin'].client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_company_already_exist(self):
        """
        POST /api/companies/ fails for company already exists
        """
        self.data = {'company_name': self.companies[0].company_name,
                     'creator_id': self.users['admin'].user.id}
        response = self.users['admin'].client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_company_missing_company_name(self):
        """
        POST /api/companies/ fails without company_name
        """
        response = self.users['admin'].client.post(self.url, {
            'creator_id': self.users['admin'].user.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIViewTestCase(BaseTestCase):
    def setUp(self):
        super(CompanyDetailAPIViewTestCase, self).setUp()
        self.test_company = create_random_company(self.users['admin'].user.id)
        self.url = '/api/companies/' + str(self.test_company.id) + '/'

    def test_get_company(self):
        """
        GET /api/companies/:company_id success
        """
        response = self.users['admin'].client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        company = json.loads(response.content)
        self.assertTrue(company)

    def test_delete_company(self):
        """
        DELETE /api/companies/:company_id success
        """
        response = self.users['admin'].client.delete(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
