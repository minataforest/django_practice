from django.urls import path
from celery_test.views import celery_test

app_name = "celery"

urlpatterns = [
    path("celery_test/", celery_test, name="celery_test"),
]
