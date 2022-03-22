from django.urls import path
from .views import videoAPIView, videosAPIView

urlpatterns = [
    path('video/', videoAPIView.as_view(), name='video'),
    path('videos/', videosAPIView.as_view(), name='videos')
]
