from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "drf"

urlpatterns = [
    path("blog/", views.BlogList.as_view()),
    path(
        "blog/<int:pk>/",
        views.BlogDetail.as_view(),
    ),
]

# view에서 사용한 format=None과, urls의 format_suffix_patterns는 세트로 붙어 다니면서
# 파일 형식 접미사를 url에서 어떻게 할 것인가를 결정짓는다.
urlpatterns = format_suffix_patterns(urlpatterns)
