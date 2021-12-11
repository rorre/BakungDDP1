from typing import List, Tuple

# flake8: noqa
# fmt: off
MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
    ["ddp 1 a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
    ["ddp 1 a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
    ["ddp 1 b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
    ["manbis",      HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
    ["matdis 1 a",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
    ["matdis 1 b",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40]
]

"""
Merepresentasikan jadwal “ddp 1 a” hari senin 08.00 sampai 09.40, serta hari rabu jam 08.00 sampai 09.40

Jadwal “ddp 1 b” hari selasa jam 08.00 sampai 09.40
Jadwal “manbis” hari senin jam 09.00 sampai 10.40
Jadwal “matdis 1 a” hari rabu jam 09.00 sampai 10.40
Jadwal “matdis 1 b” hari rabu jam 09.00 sampai 10.40
"""
# fmt: on

# Type aliases untuk static typing
Matkul = Tuple[str, int, int]
OverlapPair = Tuple[Matkul, Matkul]


def get_matkul(nama: str, subjects: List[Matkul]) -> List[Matkul]:
    """Mendapatkan jadwal-jadwal matkul berdasarkan nama dari list matkul yang diberikan"""
    result = []
    for matkul in subjects:
        # Lower kedua sisi agar menjadi lowercase,
        # sehingga checking bersifat case insensitive
        if nama.lower() == matkul[0].lower():
            result.append(matkul)
    return result


def find_overlap(subjects: List[Matkul]) -> List[OverlapPair]:
    """Mencari bentrok/overlap waktu dari jadwal-jadwal yang sudah diambil"""
    # subjects = sorted(subjects, key=lambda x: x[1])
    overlaps: List[OverlapPair] = []
    # Iterasi pada setiap matkul, dan lakukan cek kepada setiap
    # matkul yang berada di posisi setelahnya apabila terjadi overlap
    # atau tidak.
    for i in range(len(subjects) - 1):
        current = subjects[i]
        current_start = current[1]
        current_end = current[2]

        # Loop untuk setiap matkul setelah matkul saat ini
        for j in range(i + 1, len(subjects)):
            target = subjects[j]
            target_start = target[1]
            target_end = target[2]

            # Cek apabila:
            #   - Matkul setelahnya dimulai sebelum/saat matkul saat ini selesai
            #   - Matkul saat ini dimulai sebelum/saat matkul setelahnya selesai
            # Apabila keduanya benar, maka terjadi bentrok/overlap.
            #
            # Contoh overlap pada matkul A dan B:
            #          Astart                    Aend
            #             |------------------------|
            #    |------------------------|
            # Bstart                    Bend
            if current_start <= target_end and target_start <= current_end:
                pair = (current, target)
                # Skip apabila data sudah terdapat di dalam overlaps
                if pair in overlaps or reversed(pair) in overlaps:
                    continue
                overlaps.append((current, target))
    return overlaps


def format_time(time: int) -> str:
    """Format waktu yang diberikan menjadi "Hari, Jam.Menit" """
    DAYS = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    day = DAYS[time // MENIT_DALAM_HARI]

    # Kurangi waktu dengan menggunakan sisa pembagian
    # menit dalam hari
    time = time % MENIT_DALAM_HARI
    hour = time // MENIT_DALAM_JAM

    # Kurangi waktu dengan menggunakan sisa pembagian
    # menit dalam jam
    time = time % MENIT_DALAM_JAM
    minute = time
    return f"{day + ',':<7} {hour:0>2}.{minute:0>2}"


selected_matkul: List[Matkul] = []
while True:
    print("=========== SUSUN JADWAL ===========")
    print("1  Add matkul")
    print("2  Drop matkul")
    print("3  Cek ringkasan")
    print("4  Lihat daftar matkul ")
    print("5  Selesai")
    print("====================================")
    print()
    option = input("Masukkan pilihan: ").strip()

    # Add matkul
    if option == "1":
        # Buang trailing dan leading space dari input
        nama_matkul = input("Masukkan nama matkul: ").strip()
        matkul_to_add = get_matkul(nama_matkul, MATKUL_TERSEDIA)  # type: ignore
        if not matkul_to_add:
            print("Matkul tidak ditemukan")
            print()
            continue

        selected_matkul.extend(matkul_to_add)

    # Drop matkul
    elif option == "2":
        # Buang trailing dan leading space dari input
        nama_matkul = input("Masukkan nama matkul: ").strip()
        matkul_to_remove = get_matkul(nama_matkul, selected_matkul)
        if not matkul_to_remove:
            print("Matkul tidak ditemukan")
            print()
            continue

        for matkul in matkul_to_remove:
            selected_matkul.remove(matkul)

    # Cek ringkasan
    elif option == "3":
        overlaps = find_overlap(selected_matkul)
        if not overlaps:
            print("Tidak ada matkul yang bermasalah")
            print()
            continue

        for overlap_pair in overlaps:
            print(f"\t{overlap_pair[0][0]} bentrok dengan {overlap_pair[1][0]}")

    # Daftar matkul
    elif option == "4":
        if not selected_matkul:
            print("Tidak ada matkul yang diambil")
            print()
            continue

        print("daftar matkul:")
        # Sortir dan print jadwal berdasarkan nama, lalu waktu mulai
        name_sorted = sorted(selected_matkul, key=lambda x: x[0])
        sorted_matkul = sorted(name_sorted, key=lambda x: x[1])
        for matkul in sorted_matkul:
            start_formatted = format_time(matkul[1])
            end_formatted = format_time(matkul[2])
            print(
                "\t{0:<14}{1} s/d {2}".format(
                    matkul[0].upper(), start_formatted, end_formatted
                )
            )

    # Selesai
    elif option == "5":
        print("Terima kasih!")
        break

    # Invalid input
    else:
        print("Maaf, pilihan tidak tersedia")
    print()
