from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.photo_upload, name='photo_upload'),
    path('form_cnn/', views.cnn_prediction, name='photo_upload'),
]
