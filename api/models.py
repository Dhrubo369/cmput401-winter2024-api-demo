from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    years_with_company = models.DecimalField(max_digits=5, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
