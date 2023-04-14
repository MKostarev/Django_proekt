from django.shortcuts import render
from .models import Articles



#def news(request):
#    #news = Articles.objects.all('-date')
#    #return render(request, 'news/news_home.html', {'news': news})
#
#    data = {
#        'valyes': ['some', 'hello', '123']
#    }
#    return render(request, 'news/news_home.html', data)

def index(request):
    return render(request, 'main/index.html')