from django.urls import path
from .views import *

urlpatterns = [
# 메인페이지 url
    path('', main, name='main'),
# calculator 페이지 url
    path('calculator/', calculator, name='calculator'),
]
