from rest_framework import serializers
from . import models
from django.contrib.auth.models import User 

# model serializer [similar to forms.ModelForm]

# normal serializer [similar to forms.Form]
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    mobile_number = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=255) 
    is_active = serializers.BooleanField(default=False) 
    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
    
    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        instance.__dict__.update(validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


