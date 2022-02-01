from django.db import models

class UUID(models.Model):
    uuid = models.CharField(max_length=150, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
