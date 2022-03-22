from django.shortcuts import render
from rest_framework import generics
from .models import Video
from .serializers import videoSerializer

class videoAPIView(generics.ListCreateAPIView):
    queryset=Video.objects.all()
    serializer_class=videoSerializer
class videosAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Video.objects.all()
    serializer_class=videoSerializer 

def index(request):
    video:Video.objects.all()
    return render(request, 'index.html', {'video':video})