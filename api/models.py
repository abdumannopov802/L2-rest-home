from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    DEPARTMENT_CHOICES = [
        ('sales', 'Sales'),
        ('engineering', 'Engineering'),
        ('hr', 'Human Resources'),
        # Add more choices as needed
    ]
    department_name = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    average_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.get_department_name_display()  # Returns the human-readable department name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    POSITION_CHOICES = [
        ('manager', 'Manager'),
        ('assistant', 'Assistant'),
        ('developer', 'Developer'),
        ('hr_specialist', 'HR Specialist'),
        # Add more choices as needed
    ]
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
