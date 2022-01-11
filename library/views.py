from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


def index(request):
    if request.POST.get('search'):
        search_str = request.POST['search']
        books = Book.objects.filter(Q(title__contains=search_str) | Q(author__contains=search_str))
    else:
        books = Book.objects.all()
    context = {
        'books': books,
        'user': request.user,
    }
    return render(request, 'library/index.html', context)

def view_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('library:index'))

def view_login(request):
    pass

def view_signup(request):
    pass

