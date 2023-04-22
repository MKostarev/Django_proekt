from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    #return render(request, 'main/about.html')
    data = {
        'values': ['some', 'hello', '123']
            }
    return render(request, 'main/about.html', data)

def contacts(request):
    return render(request, 'main/contacts.html')


