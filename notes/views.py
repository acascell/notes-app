from django.shortcuts import render
from rest_framework import generics
from notes.serializers import UserSerializer


# Create your views here.

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
