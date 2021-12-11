# Mencari Jadwal Kereta

<p align="center">
    <img src="https://png.pngtree.com/png-vector/20200423/ourlarge/pngtree-cute-virus-cartoon-illustration-png-image_2191780.jpg" />
</p>

Setelah Dek Depe berangkat dari stasiun yang berada di dekat rumahnya, Dek Depe pergi ke negara X, dimana para penduduk di negara tersebut sedang terjangkit sebuah virus KOPIT. Semua dokter di negara tersebut sedang kewalahan dalam menangani pasien yang terjangkit virus KOPIT. Oleh karena itu, Menteri Kesehatan Negara X meminta tolong kepada Dek Depe untuk membuat sebuah program yang dapat mengetahui rantai penyebaran virus KOPIT dari orang-orang yang terjangkit.

---

Pada Lab08 ini, Anda diminta untuk membuat suatu program yang dapat melacak persebaran virus KOPIT berdasarkan ketentuan yang diberikan.

Program akan meminta Anda untuk memasukkan informasi penularan virus KOPIT. Format masukannya adalah:

    <nama_penular> <nama_tertular>

Program akan terus meminta masukan sampai Anda memberi masukan `selesai`. **Dipastikan format masukan sesuai.**

Keterangan:

-   `<nama_penular>` merupakan nama orang yang menularkan virus tersebut (case sensitive) dan dipastikan setiap barisnya hanya terdapat satu orang penular dan namanya hanya tepat satu kata
-   `<nama_tertular>` merupakan nama orang-orang yang tertular virus oleh penular tadi (setiap nama orang tertular dipastikan tepat 1 kata dan case sensitive). Orang yang tertular dari setiap baris input bisa lebih dari 1 nama.
-   Orang yang tertular tetapi tidak menularkan ke siapapun tetap akan diinput sebagai `<nama_penular>` dengan `<nama_tertular>` string kosong.
-   `<nama_penular>` bisa muncul lebih dari 1 kali dalam baris yang berbeda.
-   Dalam setiap baris, setiap `<nama_tertular>` dijamin unik (hanya muncul 1 kali).

## Daftar Perintah

-   `RANTAI_PENYEBARAN <nama_penular>`  
     Merupakan perintah yang akan mencetak `<nama_penular>` dan seluruh orang yang tertular oleh `<nama_penular>` baik secara langsung maupun tidak. Hasil pencetakan tidak harus terurut.

-   `CEK_PENULARAN <nama_tertular> <nama_penular>`  
     Perintah yang akan mencetak apakah `<nama_tertular>` terinfeksi oleh `<nama_penular>` baik secara langsung maupun tidak langsung (ditularkan melalui orang lain yang tertular oleh nama_penular).  
     Jika `<nama_tertular>` terinfeksi oleh `<nama_penular>`, maka program akan mencetak “YA” sedangkan jika tidak, program akan mencetak “TIDAK”.

-   EXIT  
     Program akan berhenti.

## Catatan

-   Solusi tanpa menggunakan implementasi rekursif tidak akan dinilai.
-   Setiap perintah yang diberikan dipastikan sesuai dengan format penulisannya.
-   Program wajib menangani perintah yang tidak ada di daftar perintah.

## Test Cases

Contoh 1

```
Masukkan rantai penyebaran:
adam budi caca frans
budi dodo
caca elsa
budi gerrad
dodo
elsa
frans
gerrad
selesai

List perintah:
1. RANTAI_PENYEBARAN
2. CEK_PENULARAN
3. EXIT

Masukkan perintah: RANTAI_PENYEBARAN adam
Rantai penyebaran adam:
- budi
- caca
- frans
- dodo
- gerrad
- elsa
- adam

Masukkan perintah: CEK_STATUS budi dodo
Maaf perintah tidak dikenali. Masukkan perintah yang valid.

Masukkan perintah: CEK_PENULARAN budi dodo
TIDAK

Masukkan perintah: CEK_PENULARAN dodo budi
YA

Masukkan perintah: CEK_PENULARAN dodo irham
Maaf, nama irham tidak ada dalam rantai penyebaran.

Masukkan perintah: RANTAI_PENYEBARAN budi
Rantai penyebaran budi:
- budi
- gerrad
- dodo

Masukkan perintah: CEK_PENULARAN elsa adam
YA

Masukkan perintah: EXIT
Goodbye~ Semoga virus KOPIT cepat berakhir.
```

Contoh 2:

```
Masukkan rantai penyebaran:
handy irene
irene jasmine kesaf lina
kesaf
lina michael opal
michael
opal
jasmine nanda
panda rafli
rafli
sultan tariq venny wilson
handy xavier
nanda
wilson zahra
tariq
venny
xavier
zahra
selesai

List perintah:
1. RANTAI_PENYEBARAN
2. CEK_PENULARAN
3. EXIT

Masukkan perintah: RANTAI_PENYEBARAN sultan
Rantai penyebaran sultan:
- tariq
- venny
- wilson
- sultan
- zahra

Masukkan perintah: CEK_PENULARAN frans dodo
Maaf, nama frans dan dodo tidak ada dalam rantai penyebaran.

Masukkan perintah: RANTAI_PENYEBARAN kesaf
Rantai penyebaran kesaf:
- kesaf

Masukkan perintah: RANTAI_PENYEBARAN irene
Rantai penyebaran irene:
- jasmine
- kesaf
- lina
- michael
- opal
- nanda
- irene

Masukkan perintah: CEK_PENULARAN zahra sultan
YA

Masukkan perintah: RANTAI_PENYEBARAN adam
Maaf, nama adam tidak ada dalam rantai penyebaran.

Masukkan perintah: RANTAI_MAKANAN adam
Maaf perintah tidak dikenali. Masukkan perintah yang valid.

Masukkan perintah: EXIT
Goodbye~ Semoga virus KOPIT cepat berakhir.
```

---

Adapted from `Lab08.pdf`. Problem made by AAA, ITA, FWS, GN, NA.
