from django.shortcuts import render
from django.conf import settings
from .forms import PhotoUploadForm
from .models import UploadedPhoto,PredictionLog
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image
from django.db.models import Sum

import numpy as np
import os

cnn_model_path = os.path.join(settings.BASE_DIR, 'ai_models', 'cnn_mnist_model.h5')
cnn_model = load_model(cnn_model_path)

def test(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
    else:
        form = PhotoUploadForm()
    
    return render(request, 'tebak_angka/form_test.html', {'form': form})

def cnn_prediction(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_photo = form.save()
            image_path = uploaded_photo.photo.path
            # convert L means Grayscale
            img = Image.open(image_path).convert('L').resize((28, 28))
            img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0

            predictions = cnn_model.predict(img_array)
            result = np.argmax(predictions, axis=1)  
            
            confidence_score = np.max(predictions)

            return render(request, 'tebak_angka/result.html', 
                          {'result': result , 
                           'confidence_score': confidence_score,
                            'uploaded_photo_url': uploaded_photo.photo.url,  
                           })
    else:
        form = PhotoUploadForm()
    
    return render(request, 'tebak_angka/cnn_predict.html', {'form': form})

def cnn_prediction_log(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_photo = form.save()
            image_path = uploaded_photo.photo.path
            img = Image.open(image_path).convert('L').resize((28, 28))
            img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0

            # Prediksi dengan model
            predictions = cnn_model.predict(img_array)
            result = np.argmax(predictions, axis=1)  # Sesuaikan dengan kebutuhan output model
            confidence_score = np.max(predictions)

            # Simpan log prediksi
            log = PredictionLog.objects.create(
                photo=uploaded_photo,
                prediction=str(result[0]),
                confidence_score=confidence_score
            )

            return render(request, 'tebak_angka/result.html', {
                'result': result,
                'confidence_score': confidence_score,
                'uploaded_photo_url': uploaded_photo.photo.url,
                'price': log.price
            })
    else:
        form = PhotoUploadForm()
    
    return render(request, 'tebak_angka/form_cnn_with_log.html', {'form':form})

def prediction_log_list(request):
    # Ambil semua log prediksi
    logs = PredictionLog.objects.all().order_by('-created_at')  # Urutkan berdasarkan waktu terbaru
    total_hits = PredictionLog.objects.count()
    total_cost = PredictionLog.objects.aggregate(total_cost=Sum('price'))['total_cost']

    return render(request, 'tebak_angka/prediction_log_list.html', {
        'logs': logs,
        'total_hits': total_hits,
        'total_cost': total_cost
    })


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
