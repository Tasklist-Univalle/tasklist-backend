from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To do"),
        ("doing", "Doing"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="todo")
    due_date = models.DateField(null=True, blank=True)  # para filtrar "Hoy"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title