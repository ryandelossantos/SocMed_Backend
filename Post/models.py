from django.db import models

class Post():
    Content = models.CharField(max_length=200)
    Media = models.FileField(upload_to='/Post/$Y/$M/$D')
    created_at = models.DateTimeField(auto_now=True)
    Updated_at = models.DateTimeField(auto_now=True)

class Comment():
    Content = models.CharField(max_length=150)
    Upload_at = models.DateTimeField(auto_now=True)