from django.db import models

class G_Victims(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

#================================================

class FB_Victims(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)