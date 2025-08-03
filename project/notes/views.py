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
    user_notes = models.Note.objects.filter(user=request.user).order_by('-created_at')

    # دریافت فیلتر از URL
    category_filter = request.GET.get('category')
    if category_filter:
        user_notes = user_notes.filter(category=category_filter)

    categories = models.Note.objects.filter(user=request.user).values_list('category', flat=True).distinct()

    return render(request, 'notes/dashboard.html', {
        'notes': user_notes,
        'categories': categories,
        'active_category': category_filter,
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
