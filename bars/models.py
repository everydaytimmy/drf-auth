
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE

class Bar(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
         return self.bar