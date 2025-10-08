from rest_framework import serializers
from .models import models


# this is used to shape data that will be sent to the frontend
# if you have a database with many fields (or variables), but you only want to send a few of them to the frontend, you can use serializers to do that
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ["id", "links"]
