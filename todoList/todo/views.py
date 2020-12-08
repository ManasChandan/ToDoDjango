from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItems
# Create your views here.

def todoView(request):
    # return HttpResponse("Hello This is todoview")
    contents = ToDoItems.objects.all()
    return render(request , "todo.html" , {"contents" : contents})

def addTodo(request):
    new_item = ToDoItems( newcontents = request.POST['work'])
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodo(requets , todo_id):
    item_delete = ToDoItems.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/')