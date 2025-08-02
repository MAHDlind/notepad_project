from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'notes/index.html')

def login_page(request):
    return render(request, 'notes/login.html')

def register_page(request):
    return render(request, 'notes/register.html')

def note_page(request):
    return render(request, 'notes/note_form.html')