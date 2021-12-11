class User() :
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User
        """
        self.__user_name = user_name
        # TODO : Tambahkan kode untuk inisiasi atribut lainnya

    # TODO : lengkapi method getter
    def get_name(self) : 
        pass

    def get_tipe(self) : 
        pass

class Seller(User) : 
    def __init__(self, user_name):
        """
        Constructor untuk class Seller
        """
        # TODO : implementasikan constructor dari class Seller

    # TODO : lengkapi getter dan setter
    def get_pemasukan(self) : 
        pass

    def set_pemasukan(self) : 
        pass

    # TODO : implementasikan method untuk tambahkan_produk dan lihat_daftar_produk_saya
    # Anda boleh memodifikasi ataupun menambahkan method sesuai dengan kebutuhan
    def tambah_product(self) :
        pass

    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        for product in self.list_barang_jual : 
            # TODO : cetak tiap product dengan urutan alphabetical
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            pass
        print("-------------------------------------\n")

    def menu(self) : 
        # TODO : implementaiskan menu untuk tipe user seller
        pass
            

# TODO : implementasikan class Buyer
class Buyer(User) : 
    pass


# TODO : implementasikan class Product
class Product() : 
    pass


# method get_user dan get_product tidak perlu diubah, 
# silakan manfaatkan method ini untuk mendapatkan user dan produk yang dibutuhkan
def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

list_user = []
list_product = []

def main():
    print("Selamat datang di Dekdepedia!")
    print("Silakan memilih salah satu menu di bawah:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")

    pilih = input("Pilihan Anda: ")

    if (pilih == "1") : 
        banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
        
        print("Data akun: ")
        for i in range (banyak_user) : 
            data_user = input(str(i+1)+". ")
            # TODO : implementasikan sign up

    elif (pilih == "2") : 
        user_name_login = input("user_name : ")
        user_logged_in = get_user(user_name_login, list_user)
        #TODO : implementasikan log in

    elif (pilih == "3") : 
        print("Terima kasih telah menggunakan Dekdepedia!")
        exit()

if __name__ == "__main__":
    main()