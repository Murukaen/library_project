from django.shortcuts import render
from .models import Book
from django.db.models import Q


def index(request):
    if request.POST.get('search'):
        search_str = request.POST['search']
        books = Book.objects.filter(Q(title__contains=search_str) | Q(author__contains=search_str))
    else:
        books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'library/index.html', context)
