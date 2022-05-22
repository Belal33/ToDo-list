from django.db import models
from django.contrib.auth.models import User # built in class for user model
import uuid
# Create your models here.

class Task(models.Model):
  user = models.ForeignKey( User , on_delete=models.CASCADE, null= True, blank=True)
  id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique = True, editable=False)
  title = models.CharField(max_length=250)
  description = models.TextField( null= True, blank=True)
  complete = models.BooleanField(default= False)
  created = models.DateTimeField(auto_now_add= True) # to set date
  def __str__(self):
    return self.title
  class Meta():
    ordering =['complete']


