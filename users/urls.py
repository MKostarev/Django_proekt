from django.urls import path
from . import views

urlpatterns = [
    ##path('', views.index, name='home'),
    ##path('about', views.about, name='about'),
    ##path('contacts', views.contacts, name='contacts'),
    path('', views.users, name='users_reg.urls'),
    ##path('news/', views.news, name='news'),

]