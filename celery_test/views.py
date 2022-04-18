from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from celery_test.tasks import mul, add


def celery_test(request):
    result = mul.delay(2, 4)
    return HttpResponse(result.get())


def celery_test2(request):
    s1 = add.s(2, 4)
    result = s1.delay()
    return HttpResponse(result.get())
