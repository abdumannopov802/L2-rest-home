from django.urls import path
from .views import *
from .views import *

urlpatterns = [
    path('employee/', employee_list, name='employee_list'),
    path('employee/<int:pk>/', employee_detail, name='employee_detail'),
    path('department/', department_list, name='department_list'),
    path('department/<int:pk>/', department_detail, name='department_detail'),
]