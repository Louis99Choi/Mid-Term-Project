from django.urls import path
from page import views

urlpatterns = [  # blog app으로 넘어온 요청에 대한 처리 방식
    path("", views.index, name="index"),  # 기본 url로 들어올 시 views.py의 index함수를 실행
]
