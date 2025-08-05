from django import forms
from .models import TodoItem, TodoListDay
from django.utils import timezone


class TodoItemForm(forms.ModelForm):
    day = forms.ModelChoiceField(
        queryset=TodoListDay.objects.all(),
        empty_label="Select a day",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = TodoItem
        fields = ['title', 'is_completed', 'day']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }