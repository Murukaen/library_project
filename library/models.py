from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    def is_available(self):
        return len(Rental.objects.filter(book=self)) == 0
    def __str__(self):
        return self.title + ' - ' + self.author

class User(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    return_date = models.DateTimeField()

