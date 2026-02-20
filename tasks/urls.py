from django.urls import path
from .views import today_tasks

urlpatterns = [
    path("tasks/today/", today_tasks),
]