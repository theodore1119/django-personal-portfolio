from django.db import models

class Teaching(models.Model):
    image = models.ImageField(upload_to='teaching/images/')
    url = models.URLField(blank=True)
