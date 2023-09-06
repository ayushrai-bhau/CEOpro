from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serailizer import * 
from rest_framework import status
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          


class Signup(APIView):
    serializer_class = UserSerializer
    def get(self, request):
        data = Myuser.objects.all()
        serializer= UserSerializer(data, many= True)
        serializers_data = serializer.data
        return Response(serializers_data ,status=status.HTTP_200_OK)
    def post(self , request , format=None):
        full_name= request.data.get('full_name')
        email = request.data.get('email')
        compy=request.data.get('compy')
        password=request.data.get('password')

        full_name = UserSerializer.validated_data['full_name']
        first_name, last_name = full_name.split()

        UserSerializer.save(first_name=first_name,last_name=last_name)
        compy_name = Company.objects.filter(id=compy)[0].compy.lower()+'.com'
        domain = email.split('@')[1]
        if domain != compy_name:
            return Response({"message":"The selected company and your domain in email are not matching"})
        cm = Myuser.objects.filter(compy=compy)
        if not cm:
            crt = Myuser.objects.create(full_name=full_name,email=email,compy_id=compy)
            crt.set_password(password)
            crt.is_ceo = True
            crt.save()
        elif cm:
            crt = Myuser.objects.create(full_name=full_name,email=email,compy_id=compy)
            crt.set_password(password)
            crt.save()
        serializer = self.serializer_class(crt)

        return Response(serializer.data ,  status=status.HTTP_201_CREATED)
    
class UserPutanddeleteApi(APIView):

    permission_classes = [AllowAny]
    def get_list(self, id):
        try: 
            return Myuser.objects.get(id=id)
        except Myuser.DoesNotExist:
            raise Http404
        
    def get(self, request ,  id , format=None):
        serializer = UserSerializer(self.get_list(id))
        serializer_data = serializer.data 
        return Response(serializer_data, status= status.HTTP_200_OK)
        
    def put(self, request, id , format=None):
        print(id,'==================')
        checkList = self.get_list(id)
        serializer = UserSerializer(checkList , data=request.data)
        if serializer.is_valid():
            user_obj = serializer.save()
            user_obj.set_password(request.data.get("password"))
            user_obj.save()
            serial_data =  serializer.data
            return Response(serial_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def delete(self, request, id , format = None):
        checkList = self.get_list(id)
        checkList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
class UserallView(APIView):
   
    def get(self, request):
        data = Myuser.objects.all()
        serializer= UserwithempSerializer(data, many= True)
        serializers_data = serializer.data
        return Response(serializers_data ,status=status.HTTP_200_OK)
    
    def post(self, request ):
        data = {
            'dob': request.data.get('dob'),
          'phone_number': request.data.get('phone_number' ),
            'created_at': request.data.get('created_at'),
            'updated_at' : request.data.get('updated_at'),
            'state' : request.data.get('state'),
            'address' : request.data.get('address'),
        }
        serializers = UserwithempSerializer(data = data)
        if serializers.is_valid():
            obj = serializers.save()
            obj.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    

    