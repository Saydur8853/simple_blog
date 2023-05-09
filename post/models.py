from django.db import models
from datetime import datetime
from django.urls import reverse

# from .views import post

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def get_detail_url(self):
        return reverse("post", args=[str(self.pk)])
