from django.shortcuts import render
from .models import Articles



def news(request):
    news1 = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news1})