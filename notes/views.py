from django.shortcuts import render, redirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from notes.serializers import UserSerializer
from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')


def logout_page(request):
    return render(request, 'index.html')


def register_page(request):
    return render(request, 'register.html')


def notes_page(request):
    return render(request, 'create_notes.html')


# @jwt_required
def list_notes(request):
    return render(request, 'list_notes.html')


# Create your views here.
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


# CRUD operations for notes
class NoteList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
