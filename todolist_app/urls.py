from django.urls import path
from todolist_app import views

urlpatterns = [
    path("", views.todolist, name="todolist" ),
    path("delete/<task_id>", views.delete_task, name="delete_task"),
    path("edit/<task_id>", views.edit_task, name="edit_task"),
    path("toggle/<task_id>", views.toggle_task, name="toggle_task")
]