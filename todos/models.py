from django.db import models

# Create your models here.
from users.models import CustomUser

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todos')
    due_date = models.DateField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
