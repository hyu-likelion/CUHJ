from django.urls import path
from calculator import views


urlpatterns = [
    # 메인페이지 url
    # calculator 페이지 url
    path('', views.main, name="main"),
    path('calculator/', views.calculator, name="calculator")
]
