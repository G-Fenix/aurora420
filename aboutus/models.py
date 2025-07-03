from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='aboutus/', blank=True, null=True)

    def __str__(self):
        return self.title
