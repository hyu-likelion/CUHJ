from django import forms
from .models import Todo

class TodoForm(forms.ModelForm) :
    class Meta :
        model = Todo
        fields = ['todo']

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['todo'].widget.attrs['placeholder'] = '해야할 것을 입력하세요.'