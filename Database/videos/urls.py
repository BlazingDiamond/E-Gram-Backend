from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import models
from .views import views
from .serializers import serializers

# router = DefaultRouter()
# router.register(r"videos", views.VideoViewSet, basename="video")
urlpatterns = [
    # path("", include(router.urls)),
    path("videos/", views.VideoViewSet.as_view(), name="video-list"),
]
# this file is used to direct where the urls are going inside the videos app
