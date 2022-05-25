from xml.sax import make_parser
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ='__all__'


def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    return User.objects.create(validated_data)
        

def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
