from django.db import models


# this is the model for the videos app, it contains the fields that will be in the database
class Video(models.Model):
    links = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
