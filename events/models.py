from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    day = models.CharField(max_length=15)
    time = models.TimeField()
    image = models.ImageField(upload_to='events/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
