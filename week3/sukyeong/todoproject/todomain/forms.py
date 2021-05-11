from django import forms
from .models import TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'expiration_date', 'body']

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "What's your work?"
        self.fields['expiration_date'].widget.attrs['placeholder'] = "YYYY-MM-DD"
