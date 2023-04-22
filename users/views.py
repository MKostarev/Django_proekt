from django.shortcuts import render
from .models import User
# Create your views here.

def users(request):
    return render(request, 'users/users_reg.html')
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, 'users/success.html', {'user': user})
    else:
        return render(request, 'users/register.html')