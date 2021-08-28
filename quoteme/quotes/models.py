from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
