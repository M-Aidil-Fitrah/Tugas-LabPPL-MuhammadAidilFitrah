# Tugas 3 Praktikum (PPL) - Website Katalog Sederhana

Nama: Muhammad Aidil Fitrah
NIM: 2308107010035

## Penjelasan Singkat Program
Program ini adalah sebuah website katalog produk sederhana yang dibangun menggunakan framework web Django. Website ini tidak menggunakan database (data di-_hardcode_ pada bagian views) dan memiliki fitur sebagai berikut:

- **Homepage (`/`)**: Menampilkan pesan selamat datang di website katalog.
- **Daftar Produk (`/produk/`)**: Menampilkan daftar produk (beserta harganya) dengan minimal 3 produk.
- **Detail Produk (`/produk/<id>/`)**: Menampilkan detail informasi dari sebuah produk spesifik berdasarkan ID produk yang dipilih.
- **Kontak (`/kontak/`)**: Menampilkan informasi kontak dari admin/pemilik website.

Website ini mendemostrasikan implementasi *MVT* (Model-View-Template) dalam Django, khususnya fokus pada bagian View dan Template beserta URL Routing-nya.
