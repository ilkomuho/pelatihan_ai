
# generate mnist h5 model
1. create .ipynb file (by using jupyter lab)
2. introduction numpy
    - numpy.array
3. generate model
4. test h5 model by using cli

# integrating django with h5 model
1. django-admin startproject <project_name>
    a. python manage.py migrate
    b. python manage.py createsuperuser
        - create superuser account
            Username: <project_name>
            Email address: muh.riansyaht@uho.ac.id
            password: pelatihanuho
2. cd <project_name>
3. python manage.py startapp <folder_app>
    

4. Create a form in <folder_app>/forms.py:
    a. create uhomnist/<folder_app>/urls.py
    a. edit uhomnist/urls.py, add 
        path('', include(<folder_app>.urls))


5. update <folder_app>/views.py
    - load h5 model 
    - copy logic from cli to this file
6. update <folder_app>/forms.py
7. templates/index.html
8. templates/result.html

# add persitent layer for saving logs
1. a
2. b


# create automation test
1. a
2. b
3. c

# deployment ke server
1. install python on server
2. konfigurasi nginx
3. use the web!

# pembuatan model
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
