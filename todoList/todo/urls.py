from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path("" , views.index),
    path('addTodo' , views.addTodo),
    path('deleteTodo/<int:todo_id>' , views.deleteTodo),
]