from django.urls import path
from .views import *



urlpatterns = [
    path('', Signup.as_view()),
    path('api/<int:id>', UserPutanddeleteApi.as_view()),
    path('api', UserallView.as_view()),

     
 ]
 