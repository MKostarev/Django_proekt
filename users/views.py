from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def users(request):
    return render(request, 'users/users_reg.html')


