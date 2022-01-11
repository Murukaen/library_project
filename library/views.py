from django.shortcuts import render, get_object_or_404
from .models import Book, Reservation
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.utils import timezone


def index(request):
    if request.POST.get('search'):
        search_str = request.POST['search']
        books = Book.objects.filter(Q(title__contains=search_str) | Q(author__contains=search_str))
    else:
        books = Book.objects.all()
    context = {
        'books': books,
        'user': request.user,
        'search_str': search_str
    }
    return render(request, 'library/index.html', context)

def view_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('library:index'))

def view_login(request):
    if request.method == 'GET':
        return render(request, 'library/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('library:index'))
        else:
            return render(request, 'library/login.html', {
                'error_msg': 'Login failed'
            })

def reserve(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'GET':
        return render(request, 'library/reserve.html', {
            'book': book,
            'user': request.user,
        })
    else:
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('library:login'))
        else:
            reservation = Reservation(book=book, user=request.user, expiry_date=timezone.now() + timezone.timedelta(weeks=1))
            reservation.save()
            return HttpResponseRedirect(reverse('library:my_books'))

def my_books(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('library:login'))
    else:
        books = [(reservation.book, reservation.expiry_date.strftime("%Y-%m-%d %H")) for reservation in Reservation.objects.filter(user=request.user)]
        print(books)
        return render(request, 'library/my_books.html', {
            'user': request.user,
            'books': books
        })
