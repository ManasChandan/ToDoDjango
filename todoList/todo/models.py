from django.db import models

# Create your models here.
class ToDoItems(models.Model):
    newcontents = models.TextField()

class items(models.Model):
    work = models.TextField()