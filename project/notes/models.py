from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Idea', 'Idea'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

