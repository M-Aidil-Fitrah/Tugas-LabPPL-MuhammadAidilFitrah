from django.shortcuts import render

# Hardcoded data untuk produk
PRODUK_DATA = [
    {
        'id': 1,
        'nama': 'Laptop ASUS ROG Strix',
        'harga': 25000000,
        'deskripsi': 'Laptop gaming spesifikasi tinggi untuk bermain game AAA dengan lancar. Dilengkapi RTX 4070 dan layar 240Hz.',
        'gambar': 'https://images.unsplash.com/photo-1593640408182-31c70c8268f5?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'stok': 12
    },
    {
        'id': 2,
        'nama': 'Mouse Logitech G502 Hero',
        'harga': 800000,
        'deskripsi': 'Mouse gaming dengan sensor presisi tinggi HERO 25K, pencahayaan RGB yang dapat disesuaikan, dan 11 tombol yang dapat diprogram.',
        'gambar': 'https://images.unsplash.com/photo-1527814050087-379381547961?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'stok': 45
    },
    {
        'id': 3,
        'nama': 'Keyboard Keychron K2',
        'harga': 1500000,
        'deskripsi': 'Keyboard mechanical wireless yang ringkas (75%) dengan switch Gateron Brown. Sangat nyaman untuk mengetik dan coding.',
        'gambar': 'https://images.unsplash.com/photo-1595225476474-87563907a212?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'stok': 20
    },
    {
        'id': 4,
        'nama': 'Monitor LG UltraGear',
        'harga': 4500000,
        'deskripsi': 'Monitor IPS 27-inch resolusi 2K (1440p) dengan Refresh Rate 144Hz. Visual tajam dan response time 1ms.',
        'gambar': 'https://images.unsplash.com/photo-1527443195645-1133f7f28990?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'stok': 8
    },
    {
        'id': 5,
        'nama': 'Headset Sony WH-1000XM5',
        'harga': 4200000,
        'deskripsi': 'Headset wireless dengan fitur Active Noise Cancelling terbaik di kelasnya. Baterai tahan hingga 30 jam.',
        'gambar': 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'stok': 15
    },
    {
        'id': 6,
        'nama': 'Microphone HyperX QuadCast',
        'harga': 1800000,
        'deskripsi': 'Microphone condenser standalone untuk streamer, podcaster, dan gamer dengan kualitas suara studio dan filter internal anti getar.',
        'gambar': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'stok': 30
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
