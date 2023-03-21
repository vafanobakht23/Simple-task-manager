from rest_framework import viewsets

from .serializers import HeroSerializer,TaskSerializer
from .models import Hero,Task


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('name')
    print(queryset)
    serializer_class = TaskSerializer