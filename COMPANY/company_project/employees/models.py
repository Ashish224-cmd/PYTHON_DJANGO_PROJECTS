from django.db import models
from companies.models import Company

class Employee(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    company_id = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
