from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BlogArticle(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
