from .serializers import Userserializer
from django.contrib.auth.models import User, auth
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from rest_framework.authtoken.models import Token
from django.core import serializers
import json
@api_view(['GET', 'POST'])
def Register(request):
    if request.method == "GET":
        queryset = User.objects.all()
        serializer_class = Userserializer(queryset, many='true')
        return Response(serializer_class.data)

    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        passw = data["password"]
        print(passw)
        passw = make_password(passw)
        data["password"] = passw

        serializer = Userserializer(data=data)
        # print(type(serializer))
        # serializer.password = User.set_password(serializer.password)
        if serializer.is_valid(raise_exception=True):

            user = serializer.save()

            # Email sending
            htmly = get_template('email.html')
            d = {'username': user.username}
            subject, from_email, to = 'welcome', 'radattani0608@gmail.com', user.email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(
                subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ###########################################
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def Login(request):

    if request.method == "POST":

        data = JSONParser().parse(request)

        username = data["username"]
        passw = data["password"]
        user = auth.authenticate(username=username, password=passw)

        if user is None:
            return Response({
                'err': "Invalid Credentials"
            })

        auth.login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        
        return JsonResponse({
            'token': token.key,
            'user':  json.dumps({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "username": user.username
            })
        })




