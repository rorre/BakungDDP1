import tkinter as tk
import tkinter.messagebox as tkmsg
import typing as t


class Product(object):
    def __init__(self, nama: str, harga: int, stok: int):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def decrease_stok(self, jumlah: int):
        """Mengurangi stok produk sejumlah `jumlah`."""
        self.__stok -= jumlah


class Buyer(object):
    def __init__(self):
        self.__daftar_beli: t.Dict[Product, int] = {}

    def add_daftar_beli(self, produk: Product, jumlah: int):
        """Menambahkan produk ke keranjang sebanyak `jumlah`"""
        if produk in self.__daftar_beli:
            self.__daftar_beli[produk] += jumlah
        else:
            self.__daftar_beli[produk] = jumlah

    def get_daftar_beli(self):
        return self.__daftar_beli


# GUI Starts from here

# Toplevel adalah sebuah class yang mirip dengan Frame namun akan terbuka
# secara terpisah dengan Window utama (jadi membuat top-level window yang
# terpisah)
class WindowLihatBarang(tk.Toplevel):
    def __init__(self, product_dict: t.Dict[str, Product], master: tk.Misc = None):
        super().__init__(master)
        self.product_dict = product_dict

        self.wm_title("Daftar Barang")
        self.create_widgets()

    def create_widgets(self):
        # Widget judul
        self.lbl_judul = tk.Label(self, text="Daftar Barang Yang Tersedia")
        self.lbl_judul.grid(row=0, column=1)

        # Definisi widget header table
        self.lbl_nama = tk.Label(self, text="Nama Produk")
        self.lbl_harga = tk.Label(self, text="Harga")
        self.lbl_stok = tk.Label(self, text="Stok Produk")

        # Posisi header table
        self.lbl_nama.grid(row=1, column=0)
        self.lbl_harga.grid(row=1, column=1)
        self.lbl_stok.grid(row=1, column=2)

        # Looping untuk melist semua produk dalam dictionary
        # Baris dimulai dari 2 sebab baris 0 dan 1 sudah dipakai untuk judul
        # dan header tabel
        i = 2
        for nama, barang in sorted(self.product_dict.items()):
            tk.Label(self, text=f"{nama}").grid(row=i, column=0)
            tk.Label(self, text=f"{barang.get_harga()}").grid(row=i, column=1)
            tk.Label(self, text=f"{barang.get_stok()}").grid(row=i, column=2)
            i += 1

        # Tombol exit
        self.btn_exit = tk.Button(self, text="EXIT", command=self.destroy)
        self.btn_exit.grid(row=i, column=1)


class WindowBeliBarang(tk.Toplevel):
    def __init__(
        self,
        buyer: Buyer,
        product_dict: t.Dict[str, Product],
        master: tk.Misc = None,
    ):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict

        self.wm_title("Beli Barang")
        self.geometry("280x135")
        self.create_widgets()

    def create_widgets(self):
        # Widget judul
        self.lbl_judul = tk.Label(self, text="Form Beli Barang")
        self.lbl_judul.grid(row=0, column=1)

        # Baris nama barang
        self.lbl_nama_barang = tk.Label(self, text="Nama Barang")
        self.ent_nama_barang = tk.Entry(self)
        self.lbl_nama_barang.grid(row=1, column=0, padx=2, pady=2)
        self.ent_nama_barang.grid(row=1, column=1, padx=2, pady=2)

        # Baris jumlah
        self.lbl_jumlah = tk.Label(self, text="Jumlah")
        self.ent_jumlah = tk.Entry(self)
        self.lbl_jumlah.grid(row=2, column=0, padx=2, pady=2)
        self.ent_jumlah.grid(row=2, column=1, padx=2, pady=2)

        # Button beli dan exit
        self.btn_beli = tk.Button(self, text="BELI", command=self.beli_barang)
        self.btn_exit = tk.Button(self, text="EXIT", command=self.destroy)
        self.btn_beli.grid(row=3, column=1, pady=2)
        self.btn_exit.grid(row=4, column=1, pady=2)

    def beli_barang(self):
        nama_barang = self.ent_nama_barang.get().strip()
        jumlah_str = self.ent_jumlah.get().strip()

        # Set retry sebagai true agar tidak di-destroy dengan
        # if condition selanjutnya kecuali apabila user memilih Cancel.
        retry = True

        # Input barang kosong
        if nama_barang == "":
            retry = tkmsg.askretrycancel(
                "BarangNotFound",
                "Nama barang tidak boleh kosong.",
            )

        # Barang tidak ada di dictionary product
        elif nama_barang not in self.product_dict:
            retry = tkmsg.askretrycancel(
                "BarangNotFound",
                f"Barang dengan nama {nama_barang} tidak ditemukan dalam BakungLapak.",
            )

        # Apabila kolom jumlah kosong
        elif jumlah_str == "":
            retry = tkmsg.askretrycancel("Error", "Jumlah tidak boleh kosong.")

        # Kolom jumlah bukan digit
        elif not jumlah_str.isdigit():
            retry = tkmsg.askretrycancel("Error", "Jumlah harus berupa angka positif.")

        elif int(jumlah_str) < 1:
            retry = tkmsg.askretrycancel("Error", "Jumlah harus bernilai minimal 1.")

        # Stok kurang atau kosong
        elif self.product_dict[nama_barang].get_stok() - int(jumlah_str) < 0:
            tkmsg.showwarning("StokEmpty", "Maaf, stok produk telah habis.")

        # Check passed
        else:
            jumlah = int(jumlah_str)
            barang = self.product_dict[nama_barang]
            buyer.add_daftar_beli(barang, jumlah)
            barang.decrease_stok(jumlah)

            self.ent_nama_barang.delete(0, tk.END)
            self.ent_jumlah.delete(0, tk.END)

            tkmsg.showinfo(
                "Berhasil!",
                f"Berhasil membeli {nama_barang} sejumlah {jumlah}",
            )

        # Apabila user meng-klik cancel, maka destroy window ini.
        if not retry:
            self.destroy()


class WindowCheckOut(tk.Toplevel):
    def __init__(self, buyer: Buyer, master: tk.Misc = None):
        super().__init__(master)
        self.daftar_dibeli = buyer.get_daftar_beli()

        self.wm_title("Daftar Barang")
        self.create_widgets()

    def create_widgets(self):
        # Judul
        self.lbl_title = tk.Label(self, text="Keranjangku")
        self.lbl_title.grid(row=0, column=1)

        # Definisi table header
        self.lbl_nama = tk.Label(self, text="Nama Produk")
        self.lbl_harga = tk.Label(self, text="Harga Barang")
        self.lbl_jumlah = tk.Label(self, text="Jumlah")

        # Set posisi table header
        self.lbl_nama.grid(row=1, column=0)
        self.lbl_harga.grid(row=1, column=1)
        self.lbl_jumlah.grid(row=1, column=2)

        # Looping untuk melist semua produk dalam dictionary keranjang
        # Baris dimulai dari 2 sebab baris 0 dan 1 sudah dipakai untuk judul
        # dan header tabel
        i = 2
        for product, jumlah in sorted(
            self.daftar_dibeli.items(), key=lambda x: x[0].get_nama()
        ):
            tk.Label(self, text=product.get_nama()).grid(row=i, column=0)
            tk.Label(self, text=product.get_harga()).grid(row=i, column=1)
            tk.Label(self, text=jumlah).grid(row=i, column=2)
            i += 1

        # Taruh pesan tidak ada barang yang dibeli apabila
        # dictionary keranjang kosong
        if not self.daftar_dibeli:
            tk.Label(self, text="Belum ada barang yang dibeli :(").grid(row=i, column=1)
            i += 1

        # Button exit
        self.btn_exit = tk.Button(self, text="EXIT", command=self.destroy)
        self.btn_exit.grid(row=i, column=1)


class MainWindow(tk.Frame):
    def __init__(
        self,
        buyer: Buyer,
        product_dict: t.Dict[str, Product],
        master: tk.Misc = None,
    ):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self,
            text="Selamat datang di BakungLapak. Silahkan pilih Menu yang tersedia",
        )

        self.btn_lihat_daftar_barang = tk.Button(
            self,
            text="LIHAT DAFTAR BARANG",
            command=self.popup_lihat_barang,
        )
        self.btn_beli_barang = tk.Button(
            self,
            text="BELI BARANG",
            command=self.popup_beli_barang,
        )
        self.btn_check_out = tk.Button(
            self,
            text="CHECK OUT",
            command=self.popup_check_out,
        )
        self.btn_exit = tk.Button(self, text="EXIT", command=self.master.destroy)

        self.label.pack()
        self.btn_lihat_daftar_barang.pack(pady=2)
        self.btn_beli_barang.pack(pady=2)
        self.btn_check_out.pack(pady=2)
        self.btn_exit.pack(pady=2)

    # menu barang yand dijual
    def popup_lihat_barang(self):
        WindowLihatBarang(self.product_dict)

    # menu beli barang
    def popup_beli_barang(self):
        WindowBeliBarang(self.buyer, self.product_dict)

    # menu riwayat barang yang dibeli
    def popup_check_out(self):
        WindowCheckOut(self.buyer)


if __name__ == "__main__":
    buyer = Buyer()

    product_dict = {
        "Kebahagiaan": Product("Kebahagiaan", 999999, 1),
        "Kunci TP3 SDA": Product("Kunci TP3 SDA", 1000000, 660),
    }

    m = MainWindow(buyer, product_dict)
    m.master.title("BakungLapak")  # type: ignore
    m.master.mainloop()
