from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import FoodSerializer
from api.models import Foods
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodSerializer
