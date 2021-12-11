# Mencari Jadwal Kereta

<p align="center">
    <img src="https://pingpoint.co.id/media/images/Ini_Sejarah_Singkat_Stasiun_Gambir_1_FILEminim.width-800.jpg" />
</p>

Pada suatu hari yang cerah, Dek Depe pergi ke sebuah stasiun dekat rumahnya untuk memandangi kereta-kereta yang sedang berhenti dan melintas di sana. Ketika Dek Depe melihat layar informasi jadwal keberangkatan kereta di dalam gedung stasiun, dia terpikir untuk membuat sebuah program yang dapat mencari jadwal kereta yang tersedia berdasarkan kelas dan jadwal keberangkatan. Dengan penuh semangat dan inspirasi, Dek Depe bergegas kembali ke rumahnya untuk membuat program tersebut menggunakan bahasa pemrograman Python!

---

Pada Lab 07 ini, Anda diminta untuk membuat suatu program untuk mencari jadwal kereta pada suatu stasiun berdasarkan kriteria yang ditentukan oleh perintah yang sudah tersedia.

Program akan meminta Anda untuk memasukkan informasi jadwal KA pada suatu stasiun. Format masukannya adalah:

`<nomor_ka> <tujuan_akhir> <jam_keberangkatan> <harga_tiket>`

Program akan terus meminta masukan sampai Anda memberi masukan "selesai". **Dipastikan format masukan sesuai**.

Program kemudian akan meminta Anda untuk memilih perintah yang tersedia.

## Daftar Perintah

-   `INFO_TUJUAN`  
     Program akan menampilkan tujuan akhir dari semua KA yang berangkat dari stasiun tersebut. Urutan keluaran tidak diperhatikan.

-   `TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>`  
     Program akan mencari jadwal berdasarkan tujuan dan kelas dari kereta. Kelas kereta ditentukan berdasarkan `<nomor_ka>`.

    -   Nomor KA 1xx adalah kelas Eksekutif.
    -   Nomor KA 2xx adalah kelas Bisnis.
    -   Nomor KA 3xx adalah kelas Ekonomi.

    Format keluaran dapat dilihat pada **Contoh Menjalankan Program**. Urutan keluaran tidak diperhatikan.

    Jika tidak ditemukan jadwal dengan `<tujuan_akhir>` dan `<kelas_kereta>` yang sesuai, maka program akan mengeluarkan

    > Tidak ada jadwal KA yang sesuai.

-   `TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>`  
     Program akan mencari jadwal berdasarkan tujuan dan jam keberangkatan maksimal kereta (inklusif). Format keluaran dapat dilihat pada **Contoh Menjalankan Program**. Urutan keluaran tidak diperhatikan.

    Jika tidak ditemukan jadwal dengan <tujuan_akhir> dan <jam_keberangkatan> yang sesuai, maka program akan mengeluarkan

    > Tidak ada jadwal KA yang sesuai.

-   `EXIT`  
     Program akan berhenti.

Format perintah harus sesuai dengan yang dijelaskan di soal. Perintah yang tidak valid akan di-handle oleh program dengan mengeluarkan

> Perintah yang dimasukkan tidak valid.

## Penjelasan Input

-   `<nomor_ka>` terdiri dari tiga digit angka dan memiliki range 100-399. Setiap jadwal dijamin memiliki `<nomor_ka>` di dalam range tersebut dan unik.
-   `<tujuan_akhir>` adalah string yang sifatnya case sensitive saat diproses oleh program.
-   `<jam_keberangkatan>` adalah integer dengan range 0-23 dan nilainya dijamin dalam range tersebut.
-   `<harga_tiket>` adalah integer.
-   `<kelas_kereta>` adalah string yang value-nya "Eksekutif", "Bisnis", atau "Ekonomi".

Untuk perintah `TUJUAN_KELAS` dan `TUJUAN_JAM` parameternya dijamin benar.

## Test Cases

Contoh 1:

```
Selamat datang! Silakan masukkan jadwal KA:
100 Jakarta 21 500000
200 Jakarta 21 350000
250 Jakarta 23 320000
300 Jakarta 22 240000
selesai

Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
4. EXIT

Masukkan perintah: INFO_TUJUAN
KA di stasiun ini memiliki tujuan akhir:
Jakarta

Masukkan perintah: TUJUAN_KELAS Jakarta Bisnis
KA 200 berangkat pukul 21 dengan harga tiket 350000
KA 250 berangkat pukul 23 dengan harga tiket 320000

Masukkan perintah: TUJUAN_JAM Jakarta 22
KA 100 berangkat pukul 21 dengan harga tiket 500000
KA 200 berangkat pukul 21 dengan harga tiket 350000
KA 300 berangkat pukul 22 dengan harga tiket 240000

Masukkan perintah: TUJUAN_KELAS Bandung Bisnis
Tidak ada jadwal KA yang sesuai

Masukkan perintah: TUJUAN_KELAS
Perintah yang dimasukkan tidak valid

Masukkan perintah: EXIT
Terima kasih sudah menggunakan program ini!
```

Contoh 2:

```
Selamat datang! Silakan masukkan jadwal KA:
200 Yogyakarta 9 200000
201 Yogyakarta 10 250000
153 Yogyakarta 8 400000
303 Yogyakarta 4 190000
305 Yogyakarta 5 175000
301 Jakarta 3 100000
selesai

Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
4. EXIT

Masukkan perintah: INFO_TUJUAN
KA di stasiun ini memiliki tujuan akhir:
Yogyakarta
Jakarta

Masukkan perintah: TUJUAN_KELAS Yogyakarta Eksekutif
KA 153 berangkat pukul 8 dengan harga tiket 400000

Masukkan perintah: TUJUAN_JAM Yogyakarta 9
KA 200 berangkat pukul 9 dengan harga tiket 200000
KA 153 berangkat pukul 8 dengan harga tiket 400000
KA 303 berangkat pukul 4 dengan harga tiket 190000
KA 305 berangkat pukul 5 dengan harga tiket 175000

Masukkan perintah: TUJUAN_KELAS Jakarta Bisnis
Tidak ada jadwal KA yang sesuai

Masukkan perintah: TUJUAN_JAM Jakarta 2
Tidak ada jadwal KA yang sesuai

Masukkan perintah: TUJUAN_WAKTU Jakarta 4
Perintah yang dimasukkan tidak valid

Masukkan perintah: naikkeretaapituttuttut
Perintah yang dimasukkan tidak valid

Masukkan perintah: EXIT
Terima kasih sudah menggunakan program ini!
```

## Ketentuan

-   Anda diwajibkan untuk menggunakan dictionary, set, dan list/tuple. Untuk list dan tuple, bisa dipilih salah satunya saja.
-   Dilarang menggunakan class. Jika kedapatan menggunakan class, maka hasil pengerjaan tidak akan dinilai.

File test tersedia di dalam folder [Test Files](Test%20Files).

---

# Bonus: Tiket Kereta Termurah

Dek Depe berhasil menyelesaikan program tersebut. Akan tetapi, dia merasa kurang puas dengannya. Karena waktu luangnya masih banyak, Dek Depe memutuskan untuk membuat fitur tambahan untuk mencari jadwal kereta dengan harga tiket termurah.

---

Dalam soal bonus ini Anda diminta untuk mengerjakan dua fitur tambahan, yaitu mencari tiket kereta termurah berdasarkan kriteria yang sama dengan perintah-perintah yang sudah ada sebelumnya.

## Perintah Tambahan

-   `TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>`
    Program akan mencari jadwal dengan harga tiket kereta termurah berdasarkan tujuan dan kelas dari kereta. Jika terdapat lebih dari 1 jadwal, maka cetak semuanya. Format keluaran dapat dilihat pada **Contoh Menjalankan Program Bonus**.
-   `TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>`
    Program akan mencari jadwal dengan harga tiket kereta termurah berdasarkan tujuan dan jam keberangkatan maksimal kereta (inklusif). Jika terdapat lebih dari 1 jadwal, maka cetak semuanya. Format keluaran dapat dilihat pada **Contoh Menjalankan Program Bonus**.

## Test Case

```
Selamat datang! Silakan masukkan jadwal KA:
100 Jakarta 21 500000
200 Jakarta 21 350000
250 Jakarta 23 320000
300 Jakarta 22 240000
selesai

Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>
4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>
6. EXIT

Masukkan perintah: TUJUAN_KELAS_TERMURAH Jakarta Bisnis
KA 250 berangkat pukul 23 dengan harga tiket 320000

Masukkan perintah: TUJUAN_JAM_TERMURAH Jakarta 22
KA 300 berangkat pukul 22 dengan harga tiket 240000

Masukkan perintah: TUJUAN_KELAS_TERMURAH Bandung Eksekutif
Tidak ada jadwal KA yang sesuai

Masukkan perintah: EXIT
Terima kasih sudah menggunakan program ini!
```

File test tersedia di dalam folder [Test Files](Test%20Files).

---

Adapted from `Lab 07.pdf`. Problem made by BYN, IA, HIS, MRT, ORI.
