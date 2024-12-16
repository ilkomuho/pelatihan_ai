
# Generate mnist h5 model
1. create .ipynb file (by using jupyter lab)
2. introduction numpy
    - numpy.array
3. generate model
4. test h5 model by using CLI

# integrating django with h5 model
1. <b> create project  </b>
   - opsi1 = django-admin startproject <dj_project> (jika gagal gunakan yang opsi2)
   - opsi2 = python -m django startproject <dj_project>
   - python manage.py migrate
   - python manage.py createsuperuser
        - create superuser account
            Username: <dj_project>
            Email address: muh.riansyaht@uho.ac.id
            password: pelatihanuho
2. cd <dj_project>
3. python manage.py startapp <dj_app>
3. Pada settings.py, tambahkan
```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR/'templates'],
        ...
    }
]
```

4. Create a form in <dj_app>/forms.py:
    - create <dj_project>/<dj_app>/urls.py
    - edit <dj_project>/urls.py, add 
        ```python
        path('', include(<dj_app>.urls))
       ```
5. load model.h5 in django views
    - test load_model <model_name>.h5 using CLI
    - if load_model in CLI success then load_model <model_name>.h5 in <dj_app>/views.py
6. update <dj_app>/forms.py
    - setup path for uploading images, open settings.py 
    ```python
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR,'media')
     ```  
7. create html form
        
7. create templates/index.html
    - if you want to add logo or another static files, just add code in <dj_project>/settings.py
    ```python
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    ```
8. create templates/result.html


# Add persitent layer for saving logs
0. konfigurasi default db dari django adalah konfigurasi sqlite
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

1. jika ingin menggunakan DB yang lebih baik dari sqlite3, maka lakukan setup configuration for mysql in `<dj_project>/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database_name',
        'USER': 'my_database_user',
        'PASSWORD': 'my_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
2. add value in .env






# Deployment ke server
1. install python on server
2. konfigurasi nginx
3. use the web!

# Pembuatan Django model
untuk membuat model lakukan
1.  buat models/UploadedPhoto
```python
from django.db import models

class UploadedPhoto(models.Model):
    photo = models.ImageField(upload_to='uploaded_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
```
2. make migrations
python manage.py makemigrations

3. lakukan migrasi
python manage.py migrate


# Create automation test
1. too be continue...