# Create your views here.
from lib2to3.pgen2.token import EQUAL
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')

    return render(request, 'login.html')


def reset(request):
    if request.user.is_authenticated == 0:
        return redirect('/login')

    if request.method == 'POST': 
        newp = request.POST['newpassword']
        newp1 = request.POST['newpassword1']
        if newp != newp1 :
            messages.info(request,'Confirm Password not matching')
            return redirect('/login/reset')
        password = request.POST['password']
        username = request.user.username
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            u = User.objects.get(username=username)
            u.set_password(newp)
            u.save()
            auth.logout(request)
            messages.info(request,'Password Changed successfully.')
            return redirect('/login')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login/reset')
    else:
        return render(request, 'reset.html')

def forgetpassword(request):
    if request.method == 'POST':
        return redirect('/login')
    else:
        return render(request, 'forgetpassword.html')


def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken !!')
                return redirect('/login/register')
            else:
                user = User(first_name=firstname, last_name=lastname, username=username, email=email)
                user.set_password(password)
                user.save()

                """"""""""""""""""""""""""""""""""""""""""""""""""
                htmly = get_template('email.html')
                d = { 'username': username }
                subject, from_email, to = 'welcome', 'radattani0608@gmail.com', email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.info(request, 'User Created')
                return redirect('/login')
        else:
            messages.info(request, 'Password not matching.')
            return redirect('/login/register')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



