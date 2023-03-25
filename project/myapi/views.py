from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view

@api_view(['GET'])
def tasksList (request):
    tasks = Task.objects.all()
    serializer  = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail (request,pk):
    task = Task.objects.get(id=pk)
    if(task == None):
        return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer  = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(self, request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)