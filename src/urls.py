from django.conf import settings
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.http import HttpResponse

urlpatterns = [
    path("adm-panel/", admin.site.urls),
    path("ping/", lambda request: HttpResponse("pong!")),
    path("v1/", include("example.urls")),
]

if settings.DEBUG:
    from rest_framework import permissions
    from drf_yasg import openapi, views

    docs_view = views.get_schema_view(
        openapi.Info(title="API documentation", default_version="v1"),
        permission_classes=(permissions.AllowAny,),
    ).with_ui("redoc", cache_timeout=0)
    urlpatterns.append(path("docs/", docs_view, name="docs"))
