from django.urls import path
from .views import *


urlpatterns = [
    path("<int:pk>/", DetailsTask.as_view()),
    path("", ListAllTasks.as_view()),
    path("create", CreateTasks.as_view()),
    path("delete/<int:pk>", DeleteTasks.as_view()),
    path("update/<int:pk>", UpdateTasks.as_view()),
    path("done_tasks", DoneTasks.as_view())
]