from django.contrib import admin
from todo.models import items,ToDoItems
# Register your models here.
admin.site.register(items)
admin.site.register(ToDoItems)