from api.companies.models import (
    Company
)


def get_company_by_name(company_name):
    """
    Return company given company name.
    """
    return Company.objects.filter(company_name=company_name).first()


def get_company_by_id(company_id):
    """
    Return companies by company_id.
    """
    return Company.objects.filter(id=company_id).first()


def get_companies():
    """
    Return companies.
    """
    return Company.objects.all()
