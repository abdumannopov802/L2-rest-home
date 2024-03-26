from rest_framework import serializers
from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_id', 'name', 'department', 'position', 'salary')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id', 'department_name', 'average_salary')
