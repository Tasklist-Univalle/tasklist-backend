from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(["GET"])
def today_tasks(request):
    today = date.today()
    qs = Task.objects.filter(due_date=today).order_by("created_at")
    return Response(TaskSerializer(qs, many=True).data)