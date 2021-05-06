from django.db import models

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=300)
    expiration_date = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.title
