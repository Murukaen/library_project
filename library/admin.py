from django.contrib import admin

from .models import Book, User, Rental

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Rental)