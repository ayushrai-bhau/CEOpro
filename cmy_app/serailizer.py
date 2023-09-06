from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *
class UserSerializer(serializers.ModelSerializer):
    compy = serializers.SerializerMethodField()
    
    class Meta:
        model = Myuser
        fields =['id','full_name','first_name','last_name','email','compy','is_ceo']
    def get_compy(self, obj):
        try:
            return obj.compy.compy
        except:
            None


class UserwithempSerializer(serializers.ModelSerializer):
    compy= serializers.SerializerMethodField()
    class Meta:
        model = Myuser
        fields =['id','full_name','compy','dob','phone_number','created_at',"updated_at",'state','address','is_ceo' ]

    def get_compy(self, obj):
        try:
            return obj.compy.compy
        except:
            None


class Compy(serializers.ModelSerializer):
    class Meta:
        models =  Company 
        fields = "__all__"