from django.shortcuts import render, redirect, get_object_or_404
from notes import forms, models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def home_page(request):
    return render(request, 'notes/home_page.html')

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'notes/login.html', {'form':form})

def register_page(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('login')
    else:
        form = forms.RegisterForm()
    return render(request, 'notes/register.html', {'form': form})

def note_page(request):
    return render(request, 'notes/note_form.html')

def logout_view(request):
    logout(request)
    return redirect('login')
login_required()


@login_required
def dashboard(request):
    category = request.GET.get('category')
    notes = models.Note.objects.filter(user=request.user)

    if category:
        notes = notes.filter(category=category)

    # جمع‌آوری لیست دسته‌بندی‌ها (یونیک)
    categories = models.Note.objects.filter(user=request.user).values_list('category', flat=True).distinct()

    return render(request, 'notes/dashboard.html', {
        'notes': notes,
        'categories': categories,
    })


@login_required
def create_note(request):
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('dashboard')
    else:
        form = forms.NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})


@login_required
def edit_note(request, note_id):
    note = get_object_or_404(models.Note, id=note_id, user=request.user)
    form = forms.NoteForm(instance=note)
    if request.method == 'POST':
        form = forms.NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(models.Note, id=note_id, user=request.user)
    note.delete()
    return redirect('dashboard')

@login_required
def note_detail(request, note_id):
    note = get_object_or_404(models.Note, id=note_id, user=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})
