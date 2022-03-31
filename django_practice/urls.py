from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("drf/", include("drf_test.urls")),
]
