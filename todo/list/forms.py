from .models import Todo
from django import forms

class ListForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        label = {
        "task" : "task",
        }
