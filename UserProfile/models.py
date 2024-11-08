from django.db import models

class UserProfile(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length= 100)
    Bio = models.TextField()
    BirthDate = models.DateField()
    