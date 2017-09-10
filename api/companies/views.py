from django.http import Http404
# import permission
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
)
from rest_framework.views import APIView

# import libs
from lib.companies.query import (
    get_company_by_id,
    get_companies
)
# import serializers
from .serializers import CompanySerializer


class CompanyListAPIView(APIView):
    serializer_class = CompanySerializer
    permissions = [AllowAny]

    def get(self, request):
        # get authorized companies
        companies = get_companies()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        new_data = serializer.validated_data
        serializer.save()
        return Response(new_data, status=HTTP_200_OK)


class CompanyDetailAPIView(APIView):
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    def get_object(self, company_id):
        company = get_company_by_id(company_id)
        if not company:
            raise Http404
        self.check_object_permissions(self.request, company)
        return company

    def get(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=HTTP_200_OK)

    def delete(self, request, company_id):
        company = self.get_object(company_id)
        company.delete()
        return Response(status=HTTP_204_NO_CONTENT)
