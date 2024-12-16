from django.db import models

class UploadedPhoto(models.Model):
    photo = models.ImageField(upload_to='uploaded_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PredictionLog(models.Model):
    photo = models.ForeignKey(UploadedPhoto, on_delete=models.CASCADE, related_name='logs')
    prediction = models.CharField(max_length=255)
    confidence_score = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=4000)
    created_at = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    name = models.CharField(max_length=255)    