from typing import Dict, List, Literal
import string


class InvalidUser(BaseException):
    """Exception untuk user parsing apabila tidak valid."""

    pass


class User:
    def __init__(self, user_name: str, tipe: Literal["BUYER", "SELLER"]):
        self.user_name = user_name
        self.tipe = tipe

    def menu(self):
        """Display menu untuk User"""
        print()
        print(f"Selamat datang {self.user_name},")
        print("berikut menu yang bisa Anda lakukan:")


class Buyer(User):
    def __init__(self, user_name: str, saldo: int):
        super().__init__(user_name, "BUYER")
        self.saldo = saldo
        self.list_barang_beli: List[Product] = []

    def decrease_saldo(self, amount):
        """Mengurangi saldo sebanyak amount"""
        self.saldo -= amount

    def menu(self):
        """Display menu untuk Buyer"""
        super().menu()

        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA")
        print("4. LOG_OUT")

        while True:
            print()
            print(f"Saldo anda {self.saldo},")

            option = input("Apa yang ingin Anda lakukan? ")
            if option == "1":
                print()
                print("Berikut merupakan daftar product di Dekdepedia")
                print("------------------------------------------------")
                print("  Nama Product  |   Harga   | Stock |  Penjual")
                print("------------------------------------------------")
                # Sortir berdasarkan nama secara ascending
                for product in sorted(list_product.values(), key=lambda x: x.nama):
                    print(
                        "{0:<16}|{1:<11}|{2:<7}|{3}".format(
                            product.nama,
                            product.harga,
                            product.stock,
                            product.seller.user_name,
                        )
                    )
                print("------------------------------------------------")

            elif option == "2":
                nama_barang = input("Masukkan barang yang ingin dibeli : ")

                # Validasi produk
                product = list_product.get(nama_barang)

                # Produk tidak ada
                if not product:
                    print(
                        f"Barang dengan nama {nama_barang} tidak ditemukan dalam Dekdepedia."
                    )
                    continue

                # Kesediaan stok
                if product.stock <= 0:
                    print("Maaf, stok produk telah habis.")
                    continue

                # Kecukupan saldo buyer untuk membeli produk
                if self.saldo < product.harga:
                    print(f"Maaf, saldo Anda tidak cukup untuk membeli {nama_barang}.")
                    continue

                # Apabila semua cek lewat, beli produk :D
                product.buy(self)
                print(
                    f"Berhasil membeli {product.nama} dari {product.seller.user_name}"
                )

            elif option == "3":
                print()
                print("Berikut merupakan barang yang saya beli")
                print("-------------------------------------")
                print("  Nama Product  |   Harga   | Penjual")
                print("-------------------------------------")
                # Sortir berdasarkan nama secara ascending
                for product in sorted(self.list_barang_beli, key=lambda x: x.nama):
                    print(
                        "{0:<16}|{1:<11}|{2}".format(
                            product.nama,
                            product.harga,
                            product.seller.user_name,
                        )
                    )
                print("-------------------------------------")

            elif option == "4":
                print(f"Anda telah keluar dari akun {self.user_name}")
                return


class Seller(User):
    def __init__(self, user_name: str):
        super().__init__(user_name, "SELLER")
        self.pemasukan = 0
        self.list_barang_jual: List[Product] = []

    def increase_pemasukan(self, amount):
        """Menambah pemasukan seller sebanyak amount"""
        self.pemasukan += amount

    def menu(self):
        """Display menu untuk Seller"""
        super().menu()
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")

        while True:
            print()
            print(f"Pemasukan anda {self.pemasukan},")

            option = input("Apa yang ingin Anda lakukan? ")
            if option == "1":
                product_data = input("Masukkan data produk : ").split()
                name = product_data[0]
                product = Product(
                    name,
                    int(product_data[1]),
                    int(product_data[2]),
                    self,
                )

                # Tambah ke list penjualan seller dan sistem
                self.list_barang_jual.append(product)
                list_product[name] = product

            elif option == "2":
                print()
                print("Berikut merupakan barang jualan saya")
                print("-------------------------------------")
                print("  Nama Product  |   Harga   | Stock")
                print("-------------------------------------")
                # Sortir berdasarkan nama secara ascending
                for product in sorted(self.list_barang_jual, key=lambda x: x.nama):
                    print(
                        "{0:<16}|{1:<11}|{2}".format(
                            product.nama,
                            product.harga,
                            product.stock,
                        )
                    )
                print("-------------------------------------")

            elif option == "3":
                print(f"Anda telah keluar dari akun {self.user_name}")
                return


class Product:
    def __init__(self, nama: str, harga: int, stock: int, seller: Seller):
        self.nama = nama
        self.harga = harga
        self.stock = stock
        self.seller = seller

    def buy(self, buyer: Buyer):
        """Beli barang ini untuk buyer."""
        # + Pemasukan untuk seller
        # - Saldo untuk pembeli
        self.seller.increase_pemasukan(self.harga)
        buyer.decrease_saldo(self.harga)

        buyer.list_barang_beli.append(self)
        self.stock -= 1


list_user: Dict[str, User] = {}
list_product: Dict[str, Product] = {}


def is_valid_username(username: str) -> bool:
    """Cek apabila username user valid atau tidak

    Spec: [A-z0-9-_]"""
    valid_characters = string.ascii_letters + string.digits + "-_"
    # Cek apakah setiap karakter berada di valid characters
    # Apabila ada yang tidak valid, maka return False.
    for character in username:
        if character not in valid_characters:
            return False
    return True


def parse_user(user: str) -> User:
    """Parse data string sign up user menjadi instance Buyer/Seller

    Me-raise exception InvalidUser apabila selama parsing ada argumen yang
    tidak valid atau tidak sesuai spec"""
    splitted_user = user.split()

    tipe = splitted_user[0]
    if tipe == "BUYER":
        # Wajib memiliki 3 argumen, kurang atau lebih itu tidak valid.
        if len(splitted_user) != 3:
            raise InvalidUser()

        username = splitted_user[1]
        try:
            # Cek validitas username dan saldo bilangan positif
            saldo = int(splitted_user[2])
            if not is_valid_username(username) or saldo <= 0:
                raise InvalidUser()
        except ValueError:
            # Argumen saldo bukan angka :/
            raise InvalidUser()

        return Buyer(username, saldo)

    elif tipe == "SELLER":
        # Wajib memiliki 2 argumen, kurang atau lebih itu tidak valid.
        if len(splitted_user) != 2:
            raise InvalidUser()

        # Cek validitas username
        username = splitted_user[1]
        if not is_valid_username(username):
            raise InvalidUser()

        return Seller(username)
    else:
        # Tipe tidak valid
        raise InvalidUser()


def main():
    while True:
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        pilih = input("Pilihan Anda: ")

        if pilih == "1":
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))

            print("Data akun:")
            for i in range(banyak_user):
                data_user = input(str(i + 1) + ". ")
                try:
                    # Parse input data user
                    user = parse_user(data_user)
                except InvalidUser:
                    # User tidak valid berdasarkan spec, skip saja.
                    print("Akun tidak valid.")
                    continue

                # Cek apabila username sudah terdaftar di dalam list
                username = user.user_name
                if username in list_user:
                    print("Username sudah terdaftar.")
                    continue

                list_user[username] = user

        elif pilih == "2":
            user_name_login = input("user_name : ")
            current_user = list_user.get(user_name_login)
            if not current_user:
                print(f"Akun dengan username {user_name_login} tidak ditemukan")
                print()
                continue

            print(
                f"Anda telah masuk dalam akun {user_name_login} sebagai {current_user.tipe}"
            )
            # Redirect ke menu dari class Seller/Buyer
            current_user.menu()

        elif pilih == "3":
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()
        print()


if __name__ == "__main__":
    main()
