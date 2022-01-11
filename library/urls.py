from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.view_logout, name='logout'),
    path('login', views.view_login, name='login'),
    path('reserve/<int:book_id>', views.reserve, name='reserve'),
]