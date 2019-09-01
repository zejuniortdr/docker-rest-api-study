from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ping/", lambda request: HttpResponse("pong!")),
    path("v1/", include("example.urls")),
]
