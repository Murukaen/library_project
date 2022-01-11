from django.contrib import admin

from .models import Book, Rental, Reservation

admin.site.register(Book)
admin.site.register(Rental)
admin.site.register(Reservation)