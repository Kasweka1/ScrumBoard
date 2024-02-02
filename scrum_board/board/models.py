from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('ToDo', 'To-Do'),
        ('InProgress', 'In Progress'),
        ('InReview', 'In Review'),
        ('Completed', 'Completed'),
    ], default='ToDo')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
