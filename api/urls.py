from django.urls import path
from .views import EmployeeList, EmployeeDetail, DepartmentList, DepartmentDetail

urlpatterns = [
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
    path('department/', DepartmentList.as_view()),
    path('department/<int:pk>/', DepartmentDetail.as_view()),

]
