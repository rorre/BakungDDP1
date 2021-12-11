# Input himpunan A dan B, lalu split berdasarkan koma
himpunan_a = input("Masukkan input himpunan A: ").split(",")
himpunan_b = input("Masukkan input himpunan B: ").split(",")

# Mulai membuat Cartesian Product
# Untuk setiap elemen di himpunan A, mulai iterasi setiap elemen di himpunan B.
cartesian_product = []
for a_elem in himpunan_a:
    for b_elem in himpunan_b:
        # Untuk setiap pasangan elemen A dan elemen B, buat "(a,b)",
        # lalu tambahkan ke list cartesian_product
        cartesian_product.append(f"({a_elem},{b_elem})")

# Gabung semua elemen cartessian product dan dipisah dengan ", "
# Lalu tambahkan kurung kurawal di sekitar.
print("{" + ", ".join(cartesian_product) + "}")
