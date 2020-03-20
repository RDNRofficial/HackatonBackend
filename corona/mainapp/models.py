from django.db import models

class User(models.Model):
    """
    name: 
    """
    name = models.CharField(max_length=50, unique=True, primary_key=True)