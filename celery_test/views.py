from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from celery_test.tasks import mul, add


def celery_test(request):
    result = mul.delay(2)
    return HttpResponse(result.get())
