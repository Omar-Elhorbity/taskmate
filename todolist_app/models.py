from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskList(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')],
        default='Medium',
        blank=True,
        null=True
    )
    due_date = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.task  + " | " + str(self.done)