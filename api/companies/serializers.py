# import libs
from lib.companies.check import is_company_already_registered
from lib.companies.create import (
    create_company
)

# import models
from api.companies.models import Company

# import serializers
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    IntegerField
)


class CompanySerializer(ModelSerializer):
    company_id = IntegerField(source='id', read_only=True)

    class Meta:
        model = Company
        fields = [
            'company_id',
            'company_name',
        ]

    def validate(self, data):
        company_name = data.get('company_name')
        if is_company_already_registered(company_name):
            raise ValidationError("This company has already registered.")
        return data

    def create(self, validated_data):
        # create company
        company = create_company(**validated_data)
        return company
