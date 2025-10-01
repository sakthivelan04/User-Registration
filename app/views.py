from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        user = User(name=name, number=number, email=email, password=password)
        user.save()
        return redirect('success')
    return render(request, 'app/register.html')


def success(request):
    return render(request, 'app/success.html')
