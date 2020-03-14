from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    path = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now=True)
    app_user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes_counter = models.IntegerField(default=0)
