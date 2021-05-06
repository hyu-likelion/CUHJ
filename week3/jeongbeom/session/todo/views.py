from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo


def read(request) :
    todos = Todo.objects.all()
    form = TodoForm()
    context = {'todos': todos, 'form' : form}

    return render(request, "todo.html", context)

def create(request) :
    form = TodoForm(request.POST)
    if form.is_valid() :
        new_todo = form.save(commit=False)
        new_todo.save()
        #return redirect('detail', new_todo.id)
        return redirect('read')
    return redirect('read')

def detail(request, id) :
    todo = get_object_or_404(Todo, pk = id)
    return render(request, 'detail.html', {'todo' : todo})

def edit(request, id) :
    edit_todo = Todo.objects.get(id = id)
    return render(request, 'edit.html', {'todo':edit_todo})

def update(request, id) :
    update_todo = Todo.objects.get(id = id)
    update_todo.todo = request.POST['todo']
    update_todo.save()
    return redirect('read')
    #return redirect('detail', update_todo.id)

def delete(request, id) :
    delete_todo = Todo.objects.get(id = id)
    delete_todo.delete()
    return redirect('read')