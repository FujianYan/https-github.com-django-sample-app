from django.conf.urls import url

from .views import (
    StageListAPIView,
    StageDetailAPIView,
    StageOrderAPIView
)

urlpatterns = [
    # url(r'^$', StageListAPIView.as_view(), name='list'),
    # url(r'^(?P<stage_id>\d+)/$', StageDetailAPIView.as_view(), name='detail'),
    # url(r'^order/$', StageOrderAPIView.as_view(), name='order'),
]
