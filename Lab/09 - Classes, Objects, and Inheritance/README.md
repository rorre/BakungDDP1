# Dekdepedia

Dek Depe memiliki ide untuk membuat sebuah aplikasi e-commerce terinspirasi dari namanya. Dekdepedia adalah sebuah e-commerce yang menghubungkan penjual dan pembeli. Kali ini, Dek Depe meminta bantuan kalian untuk membuat sebuah platform e-commerce. Hanya saja, karena budget Dek Depe sangat terbatas, kamu hanya perlu membuat aplikasinya dalam bentuk CLI (Command Line Interface). Dek Depe ingin kamu membuat fitur-fitur fundamental yang ada dalam aplikasi e-commerce, yaitu:

-   Sebagai pembeli:

    -   Melihat semua produk
    -   Membeli produk
    -   Melihat riwayat pembelian

-   Sebagai penjual:
    -   Menambahkan produk
    -   Melihat daftar produk yang ia jual

Selain fitur-fitur di atas, akan ada fitur-fitur kecil lainnya, seperti melihat saldo, Sign Up, Login, dan Logout.

## Template

Jika masih belum memahami OOP, silakan gunakan template yang kami sediakan [di sini](template.py) untuk membantu kalian dalam memahami. Template ini tidak wajib digunakan.

## Spesifikasi

-   Saat pertama dibuka, program menampilkan tiga pilihan menu:

    1. Sign Up  
       User diminta memasukkan berapa banyak akun yang ingin didaftarkan. Masukan selanjutnya adalah data user, setiap baris mewakili data satu user dengan format `<TIPE> <USERNAME>` untuk seller dan `<TIPE> <USERNAME> <SALDO>` untuk buyer. Data akun yang valid kemudian akan didaftarkan ke dalam sistem. Jika data tidak valid, tampilkan pesan yang sesuai dan akun tidak akan didaftarkan ke sistem.

        Contoh:

        ```
        Jumlah akun yang ingin didaftarkan : 3
        1. BUYER LITHA 10000
        2. SELLER ABI_DEWA69
        3. BUYER BINTANG 20000
        ```

        > 💡 Note  
        > Username terbatas pada karakter A-Z, a-z, 0-9, underscore (\_) dan dash (-). Tidak akan dipisah dengan spasi.

        > Input jumlah akun yang ingin didaftarkan dijamin bilangan bulat positif.

        > `user_name` bersifat case sensitive.

        > Data tidak valid meliputi :
        >
        > - Tipe bukan “BUYER” atau “SELLER” (case sensitive)
        > - Saldo bukan bilangan bulat positif
        > - Format tidak sesuai
        > - Terdapat karakter di luar yang ditentukan

        Contoh:

        ```
        Jumlah akun yang ingin didaftarkan : 12
        1. BUYYYER LITHA
        Akun tidak valid.
        2. SELLER ABI_DEWA69
        3. BUYER BINTANG 20000
        4. SELLER AL AL AL
        Akun tidak valid.
        5. BUYER MARKUS!
        Akun tidak valid.
        6. BUYER ABI_DEWA69 10000
        Username sudah terdaftar.
        7. BUYER ABI_DEWA69
        Akun tidak valid.
        8. BUYER LITHA -10
        Akun tidak valid.
        9. OAWHEFOWEHFWOEUFHE
        Akun tidak valid.
        10. seller SAYA
        Akun tidak valid.
        11. BUYER Abi_Dewa69 10000
        12. BUYER MLW SALDO
        Akun tidak valid.
        ```

        > Prioritas Validasi:
        >
        > - Valid atau tidak
        > - Sudah terdaftar atau belum

    2. Log In  
       User diminta memasukkan username akun untuk login. Bila username sudah terdaftar, maka tampilkan pesan `Anda telah masuk dalam akun [USERNAME] sebagai [TIPE_USER]`. Selanjutnya tampilkan menu sesuai tipe user yang telah login.  
       Bila username belum terdaftar, tampilkan pesan `Akun dengan username [USERNAME] tidak ditemukan`

    3. Exit  
       Mencetak `Terima kasih telah menggunakan Dekdepedia!` dan keluar dari program.

    > Input pemilihan menu dijamin valid (hanya 1, 2, atau 3)

-   User yang telah berhasil login akan melihat menu sesuai dengan tipe akunnya.

    -   Menu Tipe SELLER

        1. TAMBAHKAN_PRODUK  
           User diminta memasukkan data produk dengan format `<NAMA_PRODUK> <HARGA> <STOCK_TERSEDIA>`. Data yang valid akan ditambahkan sebagai produk yang dijual oleh seller tersebut. Bila ada produk yang namanya sudah terdaftar, tampilkan pesan “Produk sudah pernah terdaftar.”

            > Format input data produk dijamin valid.

        2. LIHAT_DAFTAR_PRODUK_SAYA
           Tampilkan produk jualan seller dalam bentuk tabel sebagai berikut. Urutkan berdasarkan nama produk secara ascending (A-Z).

            ```
            Berikut merupakan barang jualan saya
            -------------------------------------
            Nama Produk  |   Harga   |  Stock
            -------------------------------------
            PRODUK1        |10000      |5
            PRODUK2        |20000      |4
            -------------------------------------
            ```

        3. LOG_OUT
           Mencetak `Anda telah keluar dari akun [USERNAME]` dan kembali ke menu utama.

        > Input pemilihan menu dijamin valid (hanya 1, 2, atau 3)

    -   Menu Tipe BUYER

        1.  LIHAT_SEMUA_PRODUK  
            Tampilkan semua produk yang terdaftar dalam sistem dalam bentuk tabel sebagai berikut. Urutkan berdasarkan nama produk secara ascending (A-Z).

                Berikut merupakan daftar produk di Dekdepedia
                -----------------------------------------------
                Nama Produk   |   Harga   | Stock |  Penjual
                -----------------------------------------------
                PRODUK1        |10000      |19     |ABI_DEWA69
                PRODUK2        |10000      |0      |ABI_DEWA69
                PRODUK3        |20000      |6      |LITHA
                -----------------------------------------------

            2. BELI_PRODUK  
               Buyer diminta memasukkan nama produk yang ingin dibeli. Bila barang tersebut tidak ditemukan, cetak `Barang dengan nama [NAMA_BARANG] tidak ditemukan dalam Dekdepedia.`

                Buyer dapat membeli barang hanya jika stoknya tersedia dan saldonya mencukupi. Jika buyer berhasil membeli barang, cetak `Berhasil membeli [NAMA_BARANG] dari [PENJUAL]. `

                Saldo buyer akan berkurang dan saldo penjual akan bertambah sesuai harga barang yang dibeli. Selain itu, stok barang tersebut akan berkurang satu.

                Cetak juga pesan yang sesuai bila pembeli gagal membeli barang, seperti, `Maaf, saldo Anda tidak cukup untuk membeli [NAMA_BARANG].` atau `Maaf, stok produk telah habis.`

                > Pengecekan yang dilakukan adalah stok barang tersedia, kemudian pengecekan saldo mencukupi.

                3. RIWAYAT_PEMBELIAN_SAYA
                   Tampilkan semua produk yang pernah dibeli buyer dalam bentuk tabel sebagai berikut. Urutkan berdasarkan nama produk secara ascending (A-Z).

                ```
                Berikut merupakan barang yang saya beli
                ----------------------------------------
                Nama Produk   |   Harga   |  Penjual
                ----------------------------------------
                PRODUK1        |10000      |ABI_DEWA69
                PRODUK2        |20000      |LITHA
                ----------------------------------------
                ```

                4. LOG_OUT  
                    Mencetak `Anda telah keluar dari akun [USERNAME]` dan kembali ke menu utama.

                > Input pemilihan menu dijamin valid (hanya 1, 2, 3, atau 4)

## Keterangan Classes

1. dekdepedia.py memiliki variabel berikut:

    - list_user: berisi daftar user yang terdaftar dalam sistem Dekdepedia, user bisa berupa seller maupun buyer
    - list_product: berisi daftar produk yang terdaftar dalam sistem Dekdepedia

2. Dekdepedia CLI memiliki 4 class, yaitu :

    - Class User  
       Atribut yang dimiliki oleh class User adalah:

        1. `user_name`: merupakan nama dari tiap user
        2. `tipe`: merupakan tipe dari tiap user. Terdapat dua tipe user di Dekdepedia CLI, yaitu “BUYER” dan “SELLER”

    - Class Buyer yang merupakan turunan dari class User  
       Atribut khusus yang dimiliki oleh class Buyer adalah:

        1. `saldo`: merupakan saldo dari tiap user
        2. `list_barang_beli`: berisi daftar produk yang dibeli oleh seorang buyer

    - Class Seller yang merupakan turunan dari class User  
       Atribut khusus yang dimiliki oleh class Seller adalah:

        1. `pemasukan`: merupakan pemasukan yang didapat seller dari produk yang terjual
        2. `list_barang_jual`: berisi daftar produk yang dijual oleh seorang seller

    - Class Product  
       Atribut yang dimiliki oleh class Product adalah:

        1. `nama`: merupakan nama dari produk
        2. `harga`: merupakan harga jual produk.
        3. `stock`: merupakan stok dari produk.
        4. `seller`: merupakan penjual dari produk tersebut

## Test Cases

Contoh 1:

```
Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 1
Jumlah akun yang ingin didaftarkan : 4
Data akun:
1. SELLER S1
2. SELLER S2
3. BUYER B1 100000
4. BUYER B2 200000


Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 2
user_name : S1
Anda telah masuk dalam akun S1 sebagai SELLER

Selamat datang S1,
berikut menu yang bisa Anda lakukan:
1. TAMBAHKAN_PRODUK
2. LIHAT_DAFTAR_PRODUK_SAYA
3. LOG_OUT

Pemasukan anda 0,
Apa yang ingin Anda lakukan? 1
Masukkan data produk : azuz 10000 1

Pemasukan anda 0,
Apa yang ingin Anda lakukan? 1
Masukkan data produk : somay 5000 2

Pemasukan anda 0,
Apa yang ingin Anda lakukan? 3
Anda telah keluar dari akun S1

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 2
user_name : B1
Anda telah masuk dalam akun B1 sebagai BUYER

Selamat datang B1,
berikut menu yang bisa Anda lakukan:
1. LIHAT_SEMUA_PRODUK
2. BELI_PRODUK
3. RIWAYAT_PEMBELIAN_SAYA
4. LOG_OUT

Saldo anda 100000,
Apa yang ingin Anda lakukan? 1

Berikut merupakan daftar produk di Dekdepedia
------------------------------------------------
  Nama Produk  |   Harga    | Stock |  Penjual
------------------------------------------------
azuz           |10000       |1      |S1
somay          |5000        |2      |S1
------------------------------------------------


Saldo anda 100000,
Apa yang ingin Anda lakukan? 2
Masukkan barang yang ingin dibeli : azuz
Berhasil membeli azuz dari S1

Saldo anda 90000,
Apa yang ingin Anda lakukan? 2
Masukkan barang yang ingin dibeli : azuz
Maaf, stok produk telah habis.

Saldo anda 90000,
Apa yang ingin Anda lakukan? 1
Berikut merupakan daftar produk di Dekdepedia
------------------------------------------------
  Nama Produk  |   Harga   | Stock |  Penjual
------------------------------------------------
azuz           |10000      |0      |S1
somay          |5000       |2      |S1
------------------------------------------------

Saldo anda 90000,
Apa yang ingin Anda lakukan? 3

Berikut merupakan barang yang saya beli
-------------------------------------
  Nama Produk  |   Harga   | Penjual
-------------------------------------
azuz           |10000      |S1
-------------------------------------

Saldo anda 90000,
Apa yang ingin Anda lakukan? 4
Anda telah keluar dari akun B1

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 3
Terima kasih telah menggunakan Dekdepedia!
```

Contoh 2:

```
Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 1
Jumlah akun yang ingin didaftarkan : 4
Data akun:
1. SELLER A
2. SELLER B
3. BUYER C
Akun tidak valid.
4. BUYER C 10000

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 2
user_name : A
Anda telah masuk dalam akun A sebagai SELLER

Selamat datang A,
berikut menu yang bisa Anda lakukan:
1. TAMBAHKAN_PRODUK
2. LIHAT_DAFTAR_PRODUK_SAYA
3. LOG_OUT

Pemasukan anda 0,
Apa yang ingin Anda lakukan? 1
Masukkan data produk : oreo 3000 5

Pemasukan anda 0,
Apa yang ingin Anda lakukan? 3
Anda telah keluar dari akun A

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 2
user_name : B
Anda telah masuk dalam akun B sebagai SELLER

Selamat datang B,
berikut menu yang bisa Anda lakukan:
1. TAMBAHKAN_PRODUK
2. LIHAT_DAFTAR_PRODUK_SAYA
3. LOG_OUT

Pemasukan anda 0,
Apa yang ingin Anda lakukan? 1
Masukkan data produk : nabati 5000 3

Pemasukan anda 0,
Apa yang ingin Anda lakukan? 2

Berikut merupakan barang jualan saya
-------------------------------------
  Nama Produk  |   Harga   | Stock
-------------------------------------
nabati         |5000       |3
-------------------------------------


Pemasukan anda 0,
Apa yang ingin Anda lakukan? 3
Anda telah keluar dari akun B

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 2
user_name : D
Akun dengan user_name D tidak ditemukan

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 2
user_name : C
Anda telah masuk dalam akun C sebagai BUYER

Selamat datang C,
berikut menu yang bisa Anda lakukan:
1. LIHAT_SEMUA_PRODUK
2. BELI_PRODUK
3. RIWAYAT_PEMBELIAN_SAYA
4. LOG_OUT

Saldo anda 10000,
Apa yang ingin Anda lakukan? 1

Berikut merupakan daftar produk di Dekdepedia
------------------------------------------------
  Nama Produk  |   Harga   | Stock |  Penjual
------------------------------------------------
nabati         |5000       |3      |B
oreo           |3000       |5      |A
------------------------------------------------


Saldo anda 10000,
Apa yang ingin Anda lakukan? 2
Masukkan barang yang ingin dibeli : nabati
Berhasil membeli nabati dari B

Saldo anda 5000,
Apa yang ingin Anda lakukan? 2
Masukkan barang yang ingin dibeli : nabati
Berhasil membeli nabati dari B

Saldo anda 0,
Apa yang ingin Anda lakukan? 2
Masukkan barang yang ingin dibeli : oreo
Maaf, saldo Anda tidak cukup untuk membeli oreo

Saldo anda 0,
Apa yang ingin Anda lakukan? 3

Berikut merupakan barang yang saya beli
-------------------------------------
  Nama Produk  |   Harga   | Penjual |
-------------------------------------
nabati         |5000       |B
nabati         |5000       |B
-------------------------------------


Saldo anda 0,
Apa yang ingin Anda lakukan? 1

Berikut merupakan daftar produk di Dekdepedia
------------------------------------------------
  Nama Produk  |   Harga   | Stock |  Penjual
------------------------------------------------
nabati         |5000       |1      |B
oreo           |3000       |5      |A
------------------------------------------------


Saldo anda 0,
Apa yang ingin Anda lakukan? 4
Anda telah keluar dari akun C

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 2
user_name : B
Anda telah masuk dalam akun B sebagai SELLER

Selamat datang B,
berikut menu yang bisa Anda lakukan:
1. TAMBAHKAN_PRODUK
2. LIHAT_DAFTAR_PRODUK_SAYA
3. LOG_OUT

Pemasukan anda 10000,
Apa yang ingin Anda lakukan? 2

Berikut merupakan barang jualan saya
-------------------------------------
  Nama Produk  |   Harga   | Stock
-------------------------------------
nabati         |5000       |1
-------------------------------------


Pemasukan anda 10000,
Apa yang ingin Anda lakukan? 3
Anda telah keluar dari akun B

Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up
2. Log In
3. Exit
Pilihan Anda: 3
Terima kasih telah menggunakan Dekdepedia!
```
