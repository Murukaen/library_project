from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.view_logout, name='logout'),
    path('login', views.view_logout, name='login'),
    path('signup', views.view_logout, name='signup'),
]