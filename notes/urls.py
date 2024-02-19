from django.urls import path
from .views import UserCreate, NoteList, NoteDetail

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
]