from django.db import models

class Shell(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    color = models.TextField(max_length=100)
    size = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

