from django.shortcuts import render, redirect
from .helper import *
from .forms import UserPasswordForm
# Create your views here.
def index(request):
    password_form = UserPasswordForm()
    message_wrong = ''
    if request.method == "POST":
        password_form = UserPasswordForm(request.POST)
        if password_form.is_valid():
            message_wrong =  check(password_form['user_password'].value())
            password_form = UserPasswordForm()
            return render(request,'index.html',{"ctf":ctf,"password_form":password_form,"message_wrong":message_wrong})

    return render(request,'index.html',{"ctf":ctf,"password_form":password_form,"message_wrong":message_wrong})
