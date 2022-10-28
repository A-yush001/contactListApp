from tkinter import CASCADE
import uuid
from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE, null=True, blank=True)
    country_code=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=10)
    contact_picture=models.URLField(null=True)
    is_favourated=models.BooleanField(default=False)
    
