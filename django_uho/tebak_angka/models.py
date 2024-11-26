from django.db import models

class UploadedPhoto(models.Model):
    photo = models.ImageField(upload_to='uploaded_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
