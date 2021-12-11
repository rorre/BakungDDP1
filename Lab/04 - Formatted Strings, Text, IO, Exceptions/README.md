# Crawler Buwung

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/himjgwp-PIw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

Setelah kamu membantu Dek Depe menghitung IPK dan IPT nya, Dek Depe direkrut perusahaan sosial media ternama bernama “Buwung” karena IPKnya sangat bagus. Perusahaan tersebut memerlukan data-data kicauan pengguna untuk keperluan pendataan.

Sebagai karyawan baru, Dek Depe diminta membuat program yang bisa mengambil kicauan pengguna dan membersihkannya dari mention, hashtag, dan url yang ada dan menuliskannya kembali pada file baru.

Melihat pekerjaan baru Dek Depe cukup berat, kamu sebagai teman yang baik berinisiatif membantu pekerjaan Dek Depe untuk meringankan bebannya.

## Spesifikasi Program

Kamu diminta membuat suatu program yang bisa menerima file lalu mengubah string tertentu menjadi string lain dan menuliskan jumlah kemunculan kategori tertentu pada file output. Isi file input yang sudah diubah kemudian dicetak di file output beserta jumlah kemunculan. Input program adalah sebuah file dengan format `.txt`. Output program juga berupa file `.txt`.

1. Program harus memeriksa keberadaan isi file input. Jika file tidak ada, cetak di terminal `File input tidak ada :(`. Jika file input tidak ada, tidak perlu membuat output file. Jika file ada tapi isinya kosong (tidak mengandung karakter apa pun), cetak di terminal `File input ada tapi kosong :(`.

2. Program harus mengubah mention (substring yang diawali dengan `@` sampai bertemu whitespace) dengan `(M)`.  
   Contoh: `@DekDepeOfficial` diubah menjadi `(M)` (tanpa tanda kutip).

3. Program harus mengubah hashtag (substring yang diawali dengan `#` sampai bertemu whitespace) dengan `(H)`.  
   Contoh: `#Lab4EZ` diubah menjadi `(H)` (tanpa tanda kutip).

4. Program harus mengubah alamat URL (substring yang diawali dengan `www.` sampai bertemu whitespace) dengan `(U)`  
   Contoh: `www.buwung.id` diubah menjadi `(U)` (tanpa tanda kutip).

5. Penulisan jumlah kategori perubahan yang muncul pada teks ditulis pada file output dengan format `<jenis> : <digit>` dengan `<digit>` rata kanan (right align) dengan jarak antara `:` dan `<digit>` sebesar 5 space dengan `<digit>` berada di dalam 5 space itu. Serta, diberikan pembatas `#` sebanyak 15 buah.  
   (Untuk representasi contoh formatting yang lebih akurat, silakan cek contoh di bawah dan expected output file)

    Format: `<jenis> : ____<digit>`  
     (Tiap `_` mewakili 1 space kosong yang diisi digit yang diperlukan)

    ```
    ###############
    Mention     : ____5  (4 space, 1 digit)
    Hashtag  	: ____0 (4 space, 1 digit)
    URL        	: ___12 (3 space, 2 digit)
    ```

    Contoh formatting pada output file:

    ```
    ###############
    Mention :     5
    Hashtag :     0
    Url     :    12
    ```

6. String hasil langkah 2-5 disimpan ke dalam file output.

> **Note:**  
> Program hanya mengganti substring-substring di atas tanpa menghilangkan spasi(“ ”) dan newline (“\n”). Untuk contoh dapat dilihat pada testcase.

## Batasan

1. Nama output file dijamin valid.
2. Mention dipastikan diawali `@` dan diakhiri ' ' atau `\n`.
3. Hashtag dipastikan diawali `#` dan diakhiri ' ' atau `\n`.
4. URL dipastikan diawali `www.` dan diakhiri ' ' atau `\n`.
5. File input dipastikan tidak berisi substring `@`, `#` atau `www.` yang berada tepat setelah karakter non-spasi.  
   Contoh: File input tidak mungkin mengandung substring `k@u`, `a##a`, atau `awww.sakit`.
6. Setiap isi file input dipastikan diakhiri baris kosong.

## Test Cases

Tersedia di dalam folder [Test Files](Test%20Files).

---

Adapted from `Lab04.pdf`. Problem made by AMS, BI, NIT, TAN.
