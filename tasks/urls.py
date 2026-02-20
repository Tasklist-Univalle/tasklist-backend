from django.urls import path
from .views import today_tasks

#Enruta el endpoint

urlpatterns = [
    path("tasks/today/", today_tasks),
]