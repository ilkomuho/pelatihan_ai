from django.shortcuts import render
from django.conf import settings
from .forms import PhotoUploadForm
# from .models import PredictionLog
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image

import numpy as np
import os

# Muat model hanya sekali saat aplikasi dimulai
model_path = os.path.join(settings.BASE_DIR, 'ai_models', 'mnist_model.h5')
model = load_model(model_path)

cnn_model_path = os.path.join(settings.BASE_DIR, 'ai_models', 'cnn_mnist_model.h5')
cnn_model = load_model(model_path)

def cnn_prediction(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_photo = form.save()
            image_path = uploaded_photo.photo.path
            # convert L means Grayscale
            img = Image.open(image_path).convert('L').resize((28, 28))
            img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0

            # Prediksi dengan model
            predictions = cnn_model.predict(img_array)
            result = np.argmax(predictions, axis=1)  # Sesuaikan dengan kebutuhan output model
            confidence_score = np.max(predictions)

            return render(request, 'tebak_angka/result.html', 
                          {'result': result , 
                           'confidence_score': confidence_score,
                            'uploaded_photo_url': uploaded_photo.photo.url,  
                           })
    else:
        form = PhotoUploadForm()
    
    return render(request, 'tebak_angka/cnn_predict.html', {'form': form})

def photo_upload(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Simpan file foto yang diunggah
            uploaded_photo = form.save()

            # Path ke file foto yang diunggah
            image_path = uploaded_photo.photo.path
            img = Image.open(image_path).convert('L').resize((28, 28))
            img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0

            # Prediksi dengan model
            predictions = model.predict(img_array)
            result = np.argmax(predictions, axis=1)  # Sesuaikan dengan kebutuhan output model
            confidence_score = np.max(predictions)
            
            # simpan log
            # PredictionLog.objects.create(photo=photo, prediction=str(prediction,confidence_score))

            # Tampilkan hasil prediksi
            return render(request, 'tebak_angka/result.html', 
                          {'result': result , 
                           'confidence_score': confidence_score,
                            'uploaded_photo_url': uploaded_photo.photo.url,  
                           })
    else:
        form = PhotoUploadForm()
    
    return render(request, 'tebak_angka/upload.html', {'form': form})
