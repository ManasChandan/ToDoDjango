from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItems
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.

# def todoView(request):
#     # return HttpResponse("Hello This is todoview")
#     contents = ToDoItems.objects.all()
#     return render(request , "todo.html" , {"contents" : contents})

def index(request):
    contents = ToDoItems.objects.all()
    return render(request , "index.html" , {"contents" : contents})

def addTodo(request):
    new_item = ToDoItems( newcontents = request.POST['work'])
    new_item.save()
    # return HttpResponseRedirect('/')
    return JsonResponse({'task' : model_to_dict(new_item)})


def deleteTodo(requets , todo_id):
    item_delete = ToDoItems.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/')

def about(request):
    return render(request , "about.html")