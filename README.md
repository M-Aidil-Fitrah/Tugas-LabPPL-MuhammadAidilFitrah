# Tugas 3 Praktikum (PPL) - Website Katalog Sederhana (TechStore)

Nama: Muhammad Aidil Fitrah
NIM: 2308107010035

## Penjelasan Singkat Program
Program ini adalah sebuah website katalog produk berkonsep e-Commerce (Toko Gadget "TechStore") yang dibangun menggunakan framework web Django dan Tailwind CSS. Website ini tidak menggunakan database relasional melainkan menggunakan list *dictionary* sebagai _hardcode_ data pada bagian `views.py`. 

Meskipun sederhana, website ini didesain menggunakan UI modern dan memiliki fitur halaman sebagai berikut:

- **Homepage (`/`)**: Menampilkan Hero section selamat datang, dan section keunggulan toko (Pengiriman Cepat, Garansi, CS).
- **Katalog Produk (`/produk/`)**: Menampilkan daftar produk (6 buah produk unggulan) berbentuk Grid Card lengkap dengan gambar (diambil dari Unsplash), harga, sisa stok, dan hover effect.
- **Detail Produk (`/produk/<id>/`)**: Menampilkan detail mendalam sebuah produk berdasarkan ID-nya, disajikan dengan layout dua kolom, lengkap dengan deskripsi, gambar high-ress, dan implementasi UI *Breadcrumb* navigasi serta tombol cart/wishlist.
- **Kontak (`/kontak/`)**: Menampilkan informasi alamat lengkap, email, nomor telepon, dan simulasi UI Form kontak bagi pengguna yang ingin menghubungi tim.

Website ini mendemostrasikan implementasi *MVT* (Model-View-Template) dalam Django dengan penekanan pada UI/UX yang _responsive_ (menggunakan Tailwind CSS CDN) dan komponen visual tambahan menggunakan *FontAwesome*.
