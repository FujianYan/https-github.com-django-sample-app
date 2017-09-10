from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),

    # company base api
    url(r'^api/companies/', include("api.companies.urls")),
    # url(r'^api/companies/(?P<company_id>\d+)/stages/', include("api.stages.urls")),
]
