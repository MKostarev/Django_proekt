from django.shortcuts import render
from .models import Articles



def news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


#def about(request):
 #   return render(request, 'main/about.html')

#def contacts(request):
 #   return render(request, 'main/contacts.html')

#def users(request):
 #   return render(request, 'users/users_reg.html')

def index(request):
    data = {
        'title':'Главная страница',
        'values':['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)