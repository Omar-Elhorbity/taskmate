from django import forms
from .models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done', 'priority', 'due_date']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New Task?'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }