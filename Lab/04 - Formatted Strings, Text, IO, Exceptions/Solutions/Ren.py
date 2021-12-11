input_fname = input("Masukkan nama file input: ")
output_fname = input("Masukkan nama file output: ")

try:
    # Buka file input dan baca baris-baris yang ada
    # file otomatis tertutup setelah keluar dari block with
    # sehingga tidak perlu panggil close.
    with open(input_fname, "r") as f_input:
        input_lines = f_input.readlines()
except FileNotFoundError:
    print("File input tidak ada :(")
    input("Program selesai. Tekan enter untuk keluar...")
    exit()

if not input_lines:
    print("File input ada tapi kosong :(")
    input("Program selesai. Tekan enter untuk keluar...")
    exit()

# Buka file output yang akan ditulis
f_output = open(output_fname, "w")
mentions = hashtags = urls = 0
for line in input_lines:
    # Split baris dengan spasi
    splitted_lines = line.split()

    # Cek setiap kata apakah diawali dengan @, # atau www.
    # dan replace kata tersebut sesuai dengan ketentuan.
    # @    -> (M)
    # #    -> (H)
    # www. -> (U)
    # Lalu increment counter mention, hashtag dan url.
    new_words = []
    for word in splitted_lines:
        if word.startswith("@"):
            word = "(M)"
            mentions += 1
        elif word.startswith("#"):
            word = "(H)"
            hashtags += 1
        elif word.startswith("www."):
            word = "(U)"
            urls += 1

        # Append kata tersebut ke list kata-kata
        new_words.append(word)
    # Tulis kalimat dengan join kata-kata dengan spasi.
    f_output.write(" ".join(new_words) + "\n")

# Tulis stats yang didapat dari proses ke file
f_output.write("\n")
f_output.write("###############\n")

# Gunakan width 5 sesuai dengan ketentuan soal.
f_output.write(f"Mention : {mentions:5}\n")
f_output.write(f"Hashtag : {hashtags:5}\n")
f_output.write(f"Url     : {urls:5}\n")
f_output.close()

print(f"Output berhasil ditulis pada {output_fname}")
input("Program selesai. Tekan enter untuk keluar...")
