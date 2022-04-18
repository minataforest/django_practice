from django.urls import path
from celery_test.views import celery_test, celery_test2

app_name = "celery"

urlpatterns = [
    path("celery_test/", celery_test, name="celery_test"),
    path("celery_test2/", celery_test2, name="celery_test2"),
]
