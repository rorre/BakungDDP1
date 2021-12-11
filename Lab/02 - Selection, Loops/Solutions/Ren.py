print("Selamat datang di Kalkulator IPK!")

# Input jumlah matkul yang diambil, dan minta ulang apabila negatif.
jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
while jumlah_matkul < 0:
    print("Jumlah mata kuliah yang kamu masukkan tidak valid.")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

# Keluar dari program apabila tidak ada matkul yang diambil.
if jumlah_matkul == 0:
    print()
    print("Tidak ada mata kuliah yang diambil.")
    exit()

mutu_lulus = 0.0
mutu_total = 0.0
sks_lulus = 0
total_sks = 0

# Input data mengenai mata kuliah yang diambil sebanyak jumlah_matkul kali.
for i in range(1, jumlah_matkul + 1):
    print()
    nama_matkul = input(f"Masukkan nama mata kuliah ke-{i}: ")

    # Input SKS dan nilai matkul, minta ulang apabila negatif.
    sks_matkul = int(input(f"Masukkan jumlah SKS {nama_matkul}: "))
    while sks_matkul <= 0:
        print("Jumlah SKS yang kamu masukkan tidak valid.")
        sks_matkul = int(input(f"Masukkan jumlah SKS {nama_matkul}: "))

    nilai = float(input("Masukkan nilai yang kamu dapatkan: "))
    while nilai < 0:
        print("Nilai yang kamu masukkan tidak valid.")
        nilai = float(input("Masukkan nilai yang kamu dapatkan: "))

    # Menentukan nilai bobot sesuai dengan tabel mutu.
    if nilai >= 85:
        bobot = 4.0
    elif nilai >= 80:
        bobot = 3.7
    elif nilai >= 75:
        bobot = 3.3
    elif nilai >= 70:
        bobot = 3.0
    elif nilai >= 65:
        bobot = 2.7
    elif nilai >= 60:
        bobot = 2.3
    elif nilai >= 55:
        bobot = 2.0
    elif nilai >= 40:
        bobot = 1.0
    else:
        bobot = 0.0

    # Masukkan nilai-nilai ke variabel total.
    total_sks += sks_matkul
    mutu_total += sks_matkul * bobot

    # Apabila lulus, juga tambah nilai-nilai tersebut ke variabel lulus.
    if bobot >= 2.0:
        sks_lulus += sks_matkul
        mutu_lulus += sks_matkul * bobot

# Hitung IPT dan IPK.
# Karena SKS yang lulus dapat berupa 0, kita gunakan kondisi khusus.
ipt = mutu_total / total_sks
if sks_lulus > 0:
    ipk = mutu_lulus / sks_lulus
else:
    ipk = 0.0

print()
print(f"Jumlah SKS lulus : {sks_lulus} / {total_sks}")
print(f"Jumlah mutu lulus: {mutu_lulus:.2f} / {mutu_total:.2f}")
print(f"Total IPK kamu adalah {ipk:.2f}")
print(f"Total IPT kamu adalah {ipt:.2f}")
