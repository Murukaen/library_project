from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login


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
    print('view_login')
    if request.method == 'GET':
        print('GET')
        return render(request, 'library/login.html')
    else:
        print('POST')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('library:index'))
        else:
            return render(request, 'library/login.html', {
                'error_msg': 'Login failed'
            });
        
def view_signup(request):
    pass

