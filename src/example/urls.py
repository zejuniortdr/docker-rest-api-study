from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from example.views import ExampleViewSet


router = DefaultRouter()
router.register(r"example", ExampleViewSet)

urlpatterns = [url(r"", include(router.urls))]
