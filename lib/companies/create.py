from api.companies.models import Company


def create_company(creator_id, **validated_data):
    """
    Create a new company by creator_id and company info
    """
    company = Company.objects.create(
        **validated_data,
        creator_id=creator_id
    )
    return company
