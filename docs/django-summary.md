# tentang django
dilihat dari scope nya, django membagi kode menjadi 2 jenis
a. direktori proyek utama
b. direktori aplikasi

proyek utama berisi konfigurasi yang bersifat global seperti settings.py, urls.py.
selain itu ia memiliki templates dan folder media.

proyek utama memiliki beberapa direktori aplikasi.

# contoh struktur tree project django
my_project/
├── my_project/                # Direktori proyek utama
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Konfigurasi proyek, termasuk `MEDIA_ROOT` dan `MEDIA_URL`
│   ├── urls.py                # URL routing utama proyek
│   ├── wsgi.py
├── ai_models/            # Aplikasi Django untuk fitur unggahan foto
│   ├── mnist_model.h5
├── tebak_angka/            # Aplikasi Django untuk fitur unggahan foto
│   ├── migrations/
│   │   ├── __init__.py        # File migrasi database
│   ├── __init__.py
│   ├── admin.py               # Konfigurasi admin untuk model unggahan
│   ├── apps.py
│   ├── forms.py               # Form untuk unggahan foto
│   ├── models.py              # Model untuk menyimpan foto
│   ├── tests.py
│   ├── urls.py                # URL routing untuk app `tebak_angka`
│   ├── views.py               # View untuk menangani unggahan dan prediksi
├── templates/                 # Template HTML
│   ├── tebak_angka/
│   │   ├── upload.html        # Halaman form unggahan foto
│   │   ├── result.html        # Halaman untuk menampilkan hasil prediksi
├── media/                     # Folder untuk menyimpan file yang diunggah (dibuat otomatis)
│   ├── uploaded_photos/       # Subfolder untuk foto yang diunggah
│       ├── <uploaded_file>.jpg
├── static/                    # (Opsional) Folder untuk file statis, seperti CSS atau JS
├── manage.py                  # Perintah manajemen Django
├── requirements.txt           # Daftar dependensi (misalnya, `Django`, `tensorflow`)