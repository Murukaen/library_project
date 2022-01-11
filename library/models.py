from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    def __str__(self):
        return self.title + ' - ' + self.author

class User(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
