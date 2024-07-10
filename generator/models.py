from django.db import models


# Create your models here.
class WebPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    background_color = models.CharField(max_length=7, default="#ffffff")  # Default to white
    text_color = models.CharField(max_length=7, default="#000000")  # Default to black
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
