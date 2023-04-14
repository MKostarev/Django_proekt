from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    #return render(request, 'main/about.html')
    data = {
        'valyes': ['some', 'hello', '123']
            }
    return render(request, 'main/about.html', data)

def contacts(request):
    return render(request, 'main/contacts.html')

def news(request):
    #return render(request, 'news/news_home.html')
    data = {
        'valyes': ['some', 'hello', '123']
            }
    return render(request, 'news/news_home.html', data)


def users(request):
    return render(request, 'users/users_reg.html')
