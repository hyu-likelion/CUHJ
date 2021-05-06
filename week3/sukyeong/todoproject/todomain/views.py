from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoForm
# Create your views here.


# Front
def home(request):
    todos = TodoList.objects.all()
    return render(request, 'home.html', {'todos': todos})


# Front
def detail(request, id):
    todo = get_object_or_404(TodoList, pk=id)
    return render(request, 'detail.html', {'todo': todo})


def new(request):
    form = TodoForm()
    return render(request, 'new.html', {'form': form})


def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = form.save(commit=False)
        new_todo.save()
        return redirect('detail', new_todo.id)
    return redirect('home')


# Front
def edit(request, id):
    edit_todo = TodoList.objects.get(id=id)
    return render(request, 'edit.html', {'todo': edit_todo})


def update(request, id):
    update_todo = TodoList.objects.get(id=id)
    update_todo.title = request.POST['title']
    update_todo.expiration_date = request.POST['expiration_date']
    update_todo.body = request.POST['body']
    update_todo.save()
    return redirect('detail', update_todo.id)


def delete(request, id):
    delete_todo = TodoList.objects.get(id=id)
    delete_todo.delete()
    return redirect('home')
