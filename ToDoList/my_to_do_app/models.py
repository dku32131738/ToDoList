from django.db import models

# Create your models here.
class Todo(models.Model):
    isDone=models.BooleanField(default=False)
    content=models.CharField(max_length=255)