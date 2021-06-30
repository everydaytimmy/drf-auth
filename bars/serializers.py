from rest_framework import serializers
from .models import Bar

class BarSerializer(serializers.ModelSerializer):
   class Meta:
         fields = ('id', 'author', 'name', 'city', 'country', 'description', 'created_at')
         model = Bar