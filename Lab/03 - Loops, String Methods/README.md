# Membuat Cartesian Product

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Cartesian_Product_qtl1.svg/501px-Cartesian_Product_qtl1.svg.png" />
</p>

> Soal ini adalah untuk kelas B-F. Untuk kelas G-H, lihat [di sini](README_GH.md).

Setelah beberapa minggu berkuliah di Fasilkom, kamu merasa sangat bahagia dan bersyukur bisa menjalani kehidupan kuliahmu. Banyak materi yang telah kamu dapatkan baik di mata kuliah DDP-1 maupun di mata kuliah lainnya.

Karena kamu masih semester 1, kamu merasa kamu masih punya cukup banyak waktu luang sehingga kamu pun iseng-iseng mulai mempelajari materi semester 2.

Kamu menemukan materi Cartesian Product yang menurutmu cukup menarik. Menurutmu, materi ini cukup relevan dengan materi yang baru saja kamu pelajari di DDP-1 tentang String dan Loops. Kamu pun penasaran dan mencoba untuk membuat program yang dapat memudahkan kamu membuat Cartesian Product.

---

## Cartesian Product

Misalkan terdapat dua himpunan A dan B, produk kartesius (Cartesian product) dari himpunan A dan B adalah himpunan A x B berikut:

> A x B = `{ (a,b) | a ∈ A ^ b ∈ B }`

### Langkah-langkah

Misal diberikan himpunan `A = { x, y }` dan himpunan `B = { a, b }` (Perhatikan bahwa isi dari himpunan A dan himpunan B bisa berupa apapun selain list, dictionary, dan tuple). Maka Cartesian Product dari himpunan A dan B ( A x B ) adalah sebagai berikut:

1. Asumsikan bahwa input pertama pada kedua himpunan tersebut merupakan elemen pertama, dan seterusnya (karena tidak ada ordering dalam himpunan). Pasangkan elemen pertama himpunan A dengan elemen pertama himpunan B, menjadi `(x,a)`

    > A x B = { (x,a) }

2. Karena di himpunan B masih terdapat elemen lain, maka pasangkan elemen pertama himpunan A dengan elemen himpunan B tersebut, menjadi `(x,b)`

    > A x B = { (x,a), (x,b) }

3. Jika semua elemen di himpunan B sudah dipasangkan dengan elemen pertama himpunan A, maka ulangi langkah 1 dan 2 untuk elemen lain yang terdapat di himpunan A
    > A x B = { (x,a), (x,b), (y,a), (y,b) }

> **Note:**  
> Perhatikan bahwa A x B akan memiliki hasil yang berbeda dengan B x A

## TODO

-   Buatlah sebuah program yang menerima input 2 buah himpunan yaitu A dan B, kemudian mengeluarkan output berupa sebuah Cartesian Product A x B!

## Catatan

-   Cartesian Product harus selalu disimpan dalam bentuk String, **tidak boleh disimpan dalam bentuk List, Tuple, Set, atau Dictionary.** Solusi dengan menggunakan List, Tuple, Set, atau Dictionary **tidak akan dinilai.**
-   Tidak boleh menggunakan metode split bawaan Python!
-   Input setiap elemen pada himpunan dipisahkan oleh koma.

> Tip:  
> Anda dapat memisahkan setiap elemen dengan mencari koma. Anda dapat menggunakan metode find untuk menemukan index dari koma.

-   Himpunan A dan B dipastikan bukan himpunan kosong.
-   A dan B dipastikan himpunan, maka tidak ada elemen pada A maupun B yang diulang

## Test Cases

Input:

```
Masukkan input himpunan A: 1,2,3
Masukkan input himpunan B: x,y,z
```

Output:

```
A x B = {(1,x), (1,y), (1,z), (2,x), (2,y), (2,z), (3,x), (3,y), (3,z)}
```

---

Input:

```
Masukkan input himpunan A: 7,8
Masukkan input himpunan B: a,b,c
```

Output:

```
A x B = {(7,a), (7,b), (7,c), (8,a), (8,b), (8,c)}
```

---

Input:

```
Masukkan input himpunan A: ab,cd,ef
Masukkan input himpunan B: 12,34,56
```

Output:

```
A x B = {(ab,12), (ab,34), (ab,56), (cd,12), (cd,34), (cd,56), (ef,12), (ef,34), (ef,56)}
```

---

Input:

```
Masukkan input himpunan A: ab,c,de
Masukkan input himpunan B: 1,10,0
```

Output:

```
A x B = {(ab,1), (ab,10), (ab,0), (c,1), (c,10), (c,0), (de,1), (de,10), (de,0)}
```

---

Input:

```
Masukkan input himpunan A: ayam,bebek,cacing
Masukkan input himpunan B: 17,1,100
```

Output:

```
A x B = {(ayam,17), (ayam,1), (ayam,100), (bebek,17), (bebek,1), (bebek,100), (cacing,17), (cacing,1), (cacing,100)}
```

---

Adapted from `Lab03.pdf`. Problem made by BBR, VS, MIL, CEL, DRY.
