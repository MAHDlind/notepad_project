from django.db import models
from django.contrib.auth.models import User


class TodoListDay(models.Model):
    DAY_CHOICES = [
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)

    def __str__(self):
        return f"{self.day} - {self.user.username}"

class TodoItem(models.Model):
    list_day = models.ForeignKey(TodoListDay, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

