from django.urls import path
from .views import *
from .views import *

urlpatterns = [
    path('create_employee/', create_employee, name='create_employee'),
    path('get_employee/<int:pk>/', get_employee, name='employee_detail'),
    path('update_employee/<int:pk>', update_employee, name='upadte_employee'),
    path('delete_employee/<int:pk>', delete_employee, name='delete_employee')
]