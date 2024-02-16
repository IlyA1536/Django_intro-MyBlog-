from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
