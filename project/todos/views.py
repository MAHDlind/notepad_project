from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem, TodoListDay
from .forms import TodoItemForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def todo_dashboard(request):
    days = TodoListDay.objects.all().order_by('day_name')
    todos_by_day = {day: day.todos.filter(user=request.user).order_by('is_completed') for day in days}
    return render(request, 'todos/dashboard.html', {
        'todos_by_day': todos_by_day,
    })


@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Todo created successfully.")
            return redirect('todos:dashboard')
    else:
        form = TodoItemForm()
    return render(request, 'todos/create_todo.html', {'form': form})


@login_required
def toggle_todo_status(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todos:dashboard')


@login_required
def add_todo_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('dashboard')
    return redirect('dashboard')
