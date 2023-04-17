from django.db import models

# Create your models here.
class notes(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)