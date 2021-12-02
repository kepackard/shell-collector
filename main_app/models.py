from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TIMES = (
    ('M', 'Morning'),
    ('O', 'Noon'),
    ('E', 'Evening')
)

class Flair(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flairs_detail', kwargs={'pk': self.id})
class Shell(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    color = models.TextField(max_length=100)
    size = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    flairs = models.ManyToManyField(Flair)
    
    def __str__(self):
        return self.name
  
    def get_absolute_url(self):
        return reverse("detail", kwargs={"shell_id": self.id})

    def cleaned_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count() >= len(TIMES)

class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0])

    shell = models.ForeignKey(Shell, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']