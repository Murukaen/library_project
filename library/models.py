from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    def __str__(self):
        return self.title + ' - ' + self.author

