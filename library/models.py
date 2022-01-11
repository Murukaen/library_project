from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    def is_rented(self):
        return len(Rental.objects.filter(book=self)) > 0
    def is_reserved(self):
        return len(Reservation.objects.filter(book=self)) > 0
    def is_available(self):
        return not self.is_rented() and not self.is_reserved();
    def __str__(self):
        return self.title + ' - ' + self.author

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    return_date = models.DateTimeField()

class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()

