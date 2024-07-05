from django.db import models
from TaskCategory.models import Task_Category
from datetime import date
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription =models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date= models.DateField(default=date.today)
    task_category = models.ManyToManyField(Task_Category)
    
    def __str__(self):
        return self.taskTitle