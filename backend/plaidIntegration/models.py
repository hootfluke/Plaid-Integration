from django.db import models

# Create your models here.

class plaidUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    token = models.CharField(max_length=500, null=True, blank=True)
    access_token = models.CharField(
        max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.token