from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('users_reg/', views.users, name='users_reg'),
    path('news/', views.news, name='news'),
]