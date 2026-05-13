from django.shortcuts import render

# Hardcoded data untuk produk
PRODUK_DATA = [
    {
        'id': 1,
        'nama': 'Laptop ASUS ROG',
        'harga': 25000000,
        'deskripsi': 'Laptop gaming spesifikasi tinggi untuk bermain game AAA.'
    },
    {
        'id': 2,
        'nama': 'Mouse Logitech G502',
        'harga': 800000,
        'deskripsi': 'Mouse gaming dengan sensor presisi tinggi dan RGB.'
    },
    {
        'id': 3,
        'nama': 'Keyboard Mechanical Keychron K2',
        'harga': 1500000,
        'deskripsi': 'Keyboard mechanical wireless dengan switch gateron brown.'
    }
]

def home(request):
    return render(request, 'catalog/home.html')

def produk_list(request):
    context = {
        'produk_list': PRODUK_DATA
    }
    return render(request, 'catalog/produk_list.html', context)

def produk_detail(request, id):
    # Mencari produk berdasarkan ID
    produk_detail = None
    for p in PRODUK_DATA:
        if p['id'] == id:
            produk_detail = p
            break
            
    context = {
        'produk': produk_detail
    }
    return render(request, 'catalog/produk_detail.html', context)

def kontak(request):
    return render(request, 'catalog/kontak.html')
