from django.urls import path
from notes.views import home_page, login_page, register_page, note_page

urlpatterns = [
    path('', home_page, name='home'),
    path('notes_form', note_page, name='add_note'),
    path('loagin', login_page, name='login'),
    path('register', register_page, name='register'),
]