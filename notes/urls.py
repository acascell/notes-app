from django.urls import path
from .views import NoteList, NoteDetail, login_page, register_page, UserCreate, notes_page

urlpatterns = [
    # Frontend URL for the login page
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('create-note', notes_page, name='create-note'),

    path('user-registration/', UserCreate.as_view(), name='user-registration'),
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
]
