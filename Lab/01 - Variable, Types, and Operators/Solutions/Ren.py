import math

# Meminta radius lingkaran yang akan digunakan, lalu convert menjadi float
# Tidak menggunakan int() sebab input dapat berupa bilangan desimal
radius_str = input("Masukkan radius lingkaran: ")
radius = float(radius_str)

# Mendefinisikan panjang persegi dan segitiga, yaitu radius * 2
panjang = radius * 2

# Mulai menghitung luas masing-masing bidang
luas_segitiga = panjang * radius / 2  # p * r / 2
luas_lingkaran = math.pi * radius ** 2  # pi * r^2
luas_persegi = panjang ** 2  # p * p (atau p^2)

# Hitung luas yang diwarnai, dimulai dari layer paling atas ke bawah
luas_ungu = luas_segitiga
luas_kuning = luas_lingkaran - luas_segitiga
luas_merah = luas_persegi - luas_lingkaran

# Print semua luas warna
print(f"Luas daerah cat merah: {luas_merah:.2f}")
print(f"Luas daerah cat kuning: {luas_kuning:.2f}")
print(f"Luas daerah cat ungu: {luas_ungu:.2f}")
