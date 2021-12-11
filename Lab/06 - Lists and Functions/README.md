# Susun Jadwal

Pada lab ini, kalian diminta untuk membuat sebuah program menyusun jadwal. Kalian diharapkan dapat memahami list dan cara mengimplementasinya ke dalam program kalian.

# Spesifikasi

1.  Pertama-tama, program kalian menampilkan suatu daftar perintah yang tersedia. Perintah-perintah itu, antara lain:

    -   Add matkul
    -   Drop matkul
    -   Cek ringkasan
    -   Lihat daftar matkul
    -   Selesai

    Setiap kali pengguna memberikan input, lakukan operasi sesuai dengan opsi yang dipilih. Program akan terus-menerus meminta input dan hanya akan berhenti jika pengguna memilih opsi selesai. Tangani kasus-kasus ketika pengguna memberikan input yang tidak valid dengan umpan balik `Maaf, pilihan tidak tersedia`.

2.  Untuk mengurangi kompleksitas lab, program kalian sejak awal sudah diberikan daftar pertemuan dari setiap matkul yang tersedia secara hard-coded. Meskipun begitu, bagian hardcode yang telah diberikan dapat diubah kapan saja oleh asisten dosen ketika program kalian sedang diuji. Daftar dari setiap pertemuan didefinisikan sebagai berikut:

        [nama_matkul, start_time, end_time]

    `nama_matkul` adalah string, sedangkan `start_time` dan `end_time` merupakan integer. Daftar dari setiap pertemuan ini akan disimpan dalam variabel `MATKUL_TERSEDIA`.

3.  `start_time` dan `end_time` merupakan sebuah integer yang merepresentasikan jumlah menit dari **hari Senin pukul 00:00** sampai waktu start_time maupun end_time tersebut.  
    Misalkan terdapat pertemuan “DDP 1 A” yang dimulai pada hari Rabu, pukul 09:31 sampai hari Rabu, pukul 11:37, maka `start_time`-nya bernilai 3451. Angka ini diperoleh dari:

        2 * (24 * 60) + 9 * (60) + 31 = 3451 [dimana senin=0, selasa=1, rabu=2, dst]

    Sedangkan `end_time` dari pertemuan tersebut adalah 3577. Angka ini diperoleh dari hasil perhitungan berikut:

        2 * (24 * 60) + 11 * (60) + 37 = 3577

4.  Semua input yang diberikan oleh user pada program ini haruslah ditangani secara **case insensitive**, serta dapat mengabaikan extra **leading spaces** maupun **trailing spaces**.

5.  Ketika pengguna memilih opsi **add matkul**, pengguna akan diminta input sebuah nama matkul dan kalian harus mencari pertemuan yang sesuai kemudian menambahkannya ke dalam daftar matkul yang sudah diambil. Jika input yang diberikan tidak ada pada `MATKUL_TERSEDIA`, cetak `Matkul tidak ditemukan`. Jika matkul tersebut ada, maka program kalian tidak perlu memberikan tanggapan apa-apa. Dijamin bahwa tidak akan diberikan input nama matkul yang terdaftar di dalam matkul yang sudah diambil.

    > Manfaatkan list comprehension dan method list.extend() untuk mengerjakan bagian ini

6.  Ketika pengguna memilih opsi **drop matkul**, pengguna akan diminta input sebuah nama matkul. Carilah matkul yang sesuai dengan input dari daftar matkul yang sudah diambil. Kemudian, hapuslah matkul tersebut dari daftar matkul yang sudah diambil. Jika ternyata matkul input yang diberikan tidak ada pada daftar matkul yang sudah diambil, maka cetak `Matkul tidak ditemukan`. Jika matkul tersebut ada pada daftar yang diambil, kalian hanya perlu menghapuskannya tanpa memberikan output apapun. Untuk bagian ini, kalian dibebaskan memilih cara for-loop biasa ataupun list-comprehension.

    > Berhati-hatilah saat menghapus objek dari list ketika sedang melakukan looping!

7.  Ketika pengguna memilih opsi **cek ringkasan**, maka periksalah apakah di antara matkul yang sudah diambil terdapat pertemuan yang bentrok. Jika tidak ada matkul yang bentrok, maka cetak `Tidak ada mata kuliah yang bermasalah`. Jika ada yang bentrok, maka cetak semua kombinasi pasangan matkul yang bentrok tersebut. Program kalian bebas untuk mencetak output dalam urutan apa saja. Perhatikanlah test case yang diberikan untuk mengetahui format output ketika terdapat pasangan matkul yang bentrok.

8.  Ketika pengguna memilih opsi **lihat daftar matkul**, maka periksalah apakah ada matkul yang sudah diambil. Jika tidak ada matkul yang diambil, cetak `Tidak ada matkul yang diambil`. Jika ada matkul yang diambil, maka outputkanlah seluruh daftar pertemuan matkul yang tersedia. Perhatikan bahwa output yang diberikan haruslah dalam format yang mudah dibaca. Artinya, program harus mengubah kembali representasi integer dari `start_time` dan `end_time` menjadi format `Hari, jam.menit`. Output yang diberikan juga harus diurutkan berdasarkan `start_time` dari pertemuan tersebut. Kalian boleh memilih untuk menggunakan method `list.sort()` maupun mengimplementasikan sendiri algoritma sorting tersebut. Output yang diberikan juga harus rapi dengan menggunakan string formatting seperti yang telah dipelajari sebelumnya.

9.  Jika pengguna telah memilih opsi **Selesai**, maka cetak `Terima kasih!` dan kemudian akhirilah program tersebut.

### Code untuk poin 2

```py
MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
    ["ddp 1 a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
    ["ddp 1 a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
    ["ddp 1 b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
    ["manbis",      HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
    ["matdis 1 a",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
    ["matdis 1 b",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40]
]

"""
Merepresentasikan jadwal “ddp 1 a” hari senin 08.00 sampai 09.40, serta hari rabu jam 08.00 sampai 09.40

Jadwal “ddp 1 b” hari selasa jam 08.00 sampai 09.40
Jadwal “manbis” hari senin jam 09.00 sampai 10.40
Jadwal “matdis 1 a” hari rabu jam 09.00 sampai 10.40
Jadwal “matdis 1 b” hari rabu jam 09.00 sampai 10.40
"""

# kode Anda selanjutnya
```

## Test Cases

Isi `MATKUL_TERSEDIA`:

```py
MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["ddp 1 c", HARI[2] + JAM[8] + 0, HARI[2] +  JAM[9] + 40],
["ddp 1 b", HARI[1] + JAM[8] + 0, HARI[1] +  JAM[9] + 40],
["manbis", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
["matdis 1 a", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["matdis 1 b", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]
```

Input/Output:

```
=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 1
Masukkan nama matkul: ddp 1 a

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 1
Masukkan nama matkul: matdis 1 b

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 3
    ddp 1 a bentrok dengan matdis 1 b

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 1
Masukkan nama matkul: kalkulus 1 c

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 3
    ddp 1 a bentrok dengan matdis 1 b

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 2
Masukkan nama matkul: matdis 1 b

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 3
Tidak ada matkul yang bermasalah

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 4
daftar matkul:
    DDP 1 A       Senin,  08.00   s/d Senin,  09.40
    KALKULUS 1 C  Rabu,   10.00   s/d Rabu,   12.00

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 5
Terima kasih!
```

---

Isi `MATKUL_TERSEDIA`:

```py
MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["ddp 1 b", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["manbis", HARI[4] + JAM[13] + 1, HARI[4] + JAM[15] + 40],
["matdis 1 a", HARI[4] + JAM[9] + 0, HARI[4] + JAM[13] + 0],
["matdis 1 b", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]
```

Input/Output:

```
=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 1
Masukkan nama matkul: manbis

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 1
Masukkan nama matkul: matdis 1 a

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 3
Tidak ada matkul yang bermasalah

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 1
Masukkan nama matkul: kalkulus 1 d
Matkul tidak ditemukan

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 2
Masukkan nama matkul: kalkulus 1 c
Matkul tidak ditemukan

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 1
Masukkan nama matkul: ddp 1 a

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 3
Tidak ada matkul yang bermasalah

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 4
daftar matkul:
    DDP 1 A       Senin,  08.00   s/d Senin,  09.40
    MATDIS 1 A    Jumat,  09.00   s/d Jumat,  13.00
    MANBIS        Jumat,  13.01   s/d Jumat,  15.40

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 2
Masukkan nama matkul: ddp 1 a

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 2
Masukkan nama matkul: ddp 1 a
Matkul tidak ditemukan

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 4
daftar matkul:
    MATDIS 1 A    Jumat,  09.00   s/d Jumat,  13.00
    MANBIS        Jumat,  13.01   s/d Jumat,  15.40

=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================

Masukkan pilihan: 5
Terima kasih!
```

---

Isi `MATKUL_TERSEDIA`:

```py
MATKUL_TERSEDIA = [
["ddp 1 a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
["ddp 1 a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
["ddp 1 b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
["manbis",      HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
["matdis 1 a",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
["matdis 1 b",  HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40]
]
```

Input/Output:

```
=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================


Masukkan pilihan: 1
Masukkan nama matkul: matdis 1 b



=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================



Masukkan pilihan: 1
Masukkan nama matkul:       matdis 1 a



=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================


Masukkan pilihan:         1
Masukkan nama matkul:    manbis



=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================


Masukkan pilihan: 1
Masukkan nama matkul: ddp 1 b



=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================


Masukkan pilihan: 1
Masukkan nama matkul: ddp 1 a




=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================


Masukkan pilihan: 3
    matdis 1 b bentrok dengan manbis
    matdis 1 b bentrok dengan ddp 1 a
    matdis 1 a bentrok dengan ddp 1 a
    manbis bentrok dengan ddp 1 a



=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================


Masukkan pilihan: 4
daftar matkul:
    DDP 1 A       Senin,  08.00   s/d Senin,  09.40
    MANBIS        Senin,  09.00   s/d Senin,  10.40
    MATDIS 1 B    Senin,  09.00   s/d Senin,  10.40
    DDP 1 B       Selasa, 08.00   s/d Selasa, 09.40
    DDP 1 A       Rabu,   08.00   s/d Rabu,   09.40
    MATDIS 1 A    Rabu,   09.00   s/d Rabu,   10.40



=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul
5  Selesai
====================================


Masukkan pilihan: 5
Terima kasih!

```

---

Adapted from `Lab 06.pdf`. Problem made by HZZ, RLF, KJ, RTS.
