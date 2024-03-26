from django.urls import path
from .views import EmployeeList, EmployeeDetail, DepartmentList, DepartmentDetail
from .views import *

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
    path('department/', DepartmentList.as_view(), name='department_list'),
    path('department/<int:pk>/', DepartmentDetail.as_view()),
    # user actions
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]
