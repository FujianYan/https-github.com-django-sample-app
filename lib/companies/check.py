from api.companies.models import (
    Company
)


def is_company_already_registered(company_name):
    """
    Check if company_name has been used.
    """
    return Company.objects.filter(company_name=company_name).exists()
