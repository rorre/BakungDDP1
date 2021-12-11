import typing


happiness = anger = sadness = 50


# Pada tiga fungsi mood mutator dibawah, lakukan
# min(100, x) untuk penjumlahan, agar value maksimal adalah 100
# max(0,   x) untuk pengurangam, agar value minimum adalah 0
def smile():
    """Modifikasi untuk emoji smile"""
    global happiness, sadness
    happiness = min(100, happiness + 9)
    sadness = max(0, sadness - 6)


def sad():
    """Modifikasi untuk emoji sad"""
    global sadness, anger
    sadness = min(100, sadness + 10)
    anger = max(0, anger - 8)


def angry():
    """Modifikasi untuk emoji angry"""
    global anger, happiness
    anger = min(100, anger + 13)
    happiness = max(0, happiness - 5)


def find_mood(
    line: str,
    mood: str,
    mood_emoji: str,
    mood_func: typing.Callable[[], None],
) -> str:
    """Mencari semua emoji yang terdapat di suatu string dan return string yang
    sudah direplace dengan emoji.

    Apabila baris tersebut dikirim oleh Pak Chanek, maka juga panggil function
    untuk meng-update value mood.
    """
    mood_str = f"({mood})"
    is_pak_chanek = line.startswith("Pak Chanek:")

    # Cari apakah index dari mood tersebut ditemukan
    mood_idx = line.find(mood_str)
    while mood_idx != -1:
        # Replace mood dengan unicode emoji, namun cukup satu occurance saja.
        # Hal ini dilakukan untuk dapat melakukan modifikasi value mood
        # sesuai dengan jumlah emoji yang dikirimkan
        line = line.replace(mood_str, mood_emoji, 1)

        # Modifikasi mood apabila baris dikirimkan oleh Pak Chanek
        if is_pak_chanek:
            mood_func()
        mood_idx = line.find(mood_str)
    return line


try:
    # Minta file dari input dan baca semua baris
    filename = input("Masukkan nama file input: ")
    with open(filename, "r") as f:
        # Baca file, lalu strip apabila file terdapat spasi atau
        # carriage returns di awal atau akhir
        contents = f.read().strip()
        lines = contents.splitlines()

    # Assertion akan gagal dan me-raise AssertionError
    # apabila lines == 0 (file kosong)
    assert len(lines) != 0
except FileNotFoundError:
    print("File input tidak ada :(")
    exit()
except AssertionError:
    print("File input ada tapi kosong :(")
    exit()

print()
for line in lines:
    # Proses percakapan per baris, cari emoji, juga
    # mereplace dan mengubah value mood apabila ditemukan
    line = line.strip()
    line = find_mood(line, "smile", "\U0001f603", smile)
    line = find_mood(line, "sad", "\U0001f622", sad)
    line = find_mood(line, "angry", "\U0001f621", angry)

    # Print baris hasil modifikasi emoji
    print(line)

# Cari nilai tertinggi dari ketiga mood
highest_value = max(happiness, sadness, anger)

# Setelah itu, compare dengan semua mood yang ada,
# apabila sama, maka tambahkan ke mood yang saat ini dirasakan.
current_moods = []
if highest_value == happiness:
    current_moods.append("bahagia")
if highest_value == sadness:
    current_moods.append("sedih")
if highest_value == anger:
    current_moods.append("marah")

# Apabila semua mood memiliki nilai yang sama, maka tidak ada
# kesimpulan yang dapat dibuat.
if len(current_moods) == 3:
    conclusion_mood = "Kesimpulan tidak ditemukan."
else:
    conclusion_mood = "Pak Chanek sedang " + " atau ".join(current_moods) + "."

# Print hasil dan kesimpulan
print()
print("Mengukur suasana hati....")
print()

print("##### Hasil Pengukuran #####")
print(f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}")
print()

print("##### Kesimpulan #####")
print(conclusion_mood)
