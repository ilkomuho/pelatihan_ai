from django.urls import path
from . import views

urlpatterns = [
    path('form_test', views.test),
    path('upload/', views.photo_upload, name='photo_upload'),
    path('form_cnn/', views.cnn_prediction, name='photo_upload'),
    path('cnn_with_log', views.cnn_prediction_log, name='cnn_prediction'),
    path('prediction_log_list', views.prediction_log_list, name='prediction_log_list'),
]