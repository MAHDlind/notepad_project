from django.urls import path
from notes.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]