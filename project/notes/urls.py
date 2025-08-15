from django.urls import path
from .views import (
    home_page, login_page, register_page,
    note_page, logout_view, dashboard,
    create_note, edit_note, delete_note,
    note_detail
)

app_name = 'notes'

urlpatterns = [
    path('', home_page, name='home'),
    path('notes_form/', note_page, name='add_note'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_note, name='create_note'),
    path('note/<int:note_id>/edit/', edit_note, name='edit_note'),
    path('note/<int:note_id>/delete/', delete_note, name='delete_note'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),
]