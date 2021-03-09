from django.db import models

class Research(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='research/images/')
    url = models.URLField(blank=True)

