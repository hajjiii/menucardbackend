from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Foods

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Foods
        fields = ['id','category', 'food_name', 'price']

