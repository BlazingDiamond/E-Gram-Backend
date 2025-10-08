from rest_framework import serializers
from .models import models


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ["id", "links"]
