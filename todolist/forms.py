from django.forms import ModelForm
from .models import Task

class create_Task(ModelForm):
    class Meta:
        model = Task;
        fields = {"title","description"}