from django.conf.urls import url

from .views import (
    CompanyListAPIView,
    CompanyDetailAPIView
)

urlpatterns = [
    url(r'^$', CompanyListAPIView.as_view(), name='list'),
    url(r'^(?P<company_id>\d+)/$', CompanyDetailAPIView.as_view(), name='detail'),
]
