from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return self.title

