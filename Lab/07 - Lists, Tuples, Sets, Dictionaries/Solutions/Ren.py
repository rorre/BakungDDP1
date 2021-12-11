schedule = {}


def find_kelas(sched, tujuan, kelas):
    """Cari jadwal berdasarkan tujuan dan kode awal kereta."""
    # Set nilai awal bergantung pada kode kereta
    # 1xx -> Eksekutif
    # 2xx -> Bisnis
    # 3xx -> Ekonomi
    # Selain itu, keluar karena tidak valid.
    if kelas == "Eksekutif":
        starting_code = 1
    elif kelas == "Bisnis":
        starting_code = 2
    elif kelas == "Ekonomi":
        starting_code = 3

    # Apabila key tidak ada di dictionary, maka return dengan empty list.
    target_sched = sched.get(tujuan, [])
    return [jadwal for jadwal in target_sched if jadwal[0] // 100 == starting_code]


def find_hour(sched, tujuan, waktu):
    """Cari jadwal berdasarkan tujuan dan waktu kereta."""
    # Apabila key tidak ada di dictionary, maka return dengan empty list.
    target_sched = sched.get(tujuan, [])
    return [jadwal for jadwal in target_sched if jadwal[2] <= waktu]


print("Selamat datang! Silakan masukkan jadwal KA:")
tujuan_list = []

# Input data hingga input yang diterima yaitu "selesai"
schedule_data = input()
while schedule_data.lower() != "selesai":
    # Split lalu convert nomor, waktu dan harga menjadi int
    data_splitted = schedule_data.split()
    data_splitted[0] = int(data_splitted[0])
    data_splitted[2] = int(data_splitted[2])
    data_splitted[3] = int(data_splitted[3])

    # Cek apabila tujuan ada di dictionary, apabila tidak,
    # buat list baru. Lalu append data input ke list.
    tujuan = data_splitted[1]
    if tujuan not in schedule:
        schedule[tujuan] = []
    schedule[tujuan].append(data_splitted)
    tujuan_list.append(tujuan)

    schedule_data = input()

print()
print("Perintah yang tersedia:")
print("1. INFO_TUJUAN")
print("2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>")
print("3. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>")
print("4. EXIT")
print()

# Convert list tujuan menjadi set agar menjadi unique
available_tujuan = set(tujuan_list)

# Format untuk print jadwal
schedule_format = "KA {0} berangkat pukul {1} dengan harga tiket {2}"
while True:
    # Terima command, lalu split command menjadi cmd dan arguments.
    # cmd merepresentasikan nama command
    # args merepresentasikan argumen/parameter dari command
    cmd_raw = input("Masukkan perintah: ")
    splitted_cmd = cmd_raw.split()
    cmd = splitted_cmd[0]
    args = splitted_cmd[1:]

    if cmd == "INFO_TUJUAN":
        print("KA di stasiun ini memiliki tujuan akhir:")
        # Print semua key dari schedule, karena key adalah tujuan.
        for target in available_tujuan:
            print(target)

    elif cmd == "TUJUAN_KELAS":
        # Cek apabila argumen berisi 2, jika tidak maka
        # keluar dari command.
        if len(args) != 2:
            print("Perintah yang dimasukkan tidak valid.")
            print()
            continue

        # Cari schedule berdasarkan tujuan dan kode awal kereta.
        tujuan, kelas = args
        filtered_schedule = find_kelas(schedule, tujuan, kelas)
        if not filtered_schedule:
            print("Tidak ada jadwal KA yang sesuai.")
            print()
            continue

        # Print semua jadwal kereta
        for sched in filtered_schedule:
            print(schedule_format.format(sched[0], sched[2], sched[3]))

    elif cmd == "TUJUAN_JAM":
        # Cek apabila argumen berisi 2, jika tidak maka
        # keluar dari command.
        if len(args) != 2:
            print("Perintah yang dimasukkan tidak valid.")
            print()
            continue

        # Cari schedule berdasarkan tujuan dan waktu.
        tujuan, waktu = args
        filtered_schedule = find_hour(schedule, tujuan, int(waktu))
        if not filtered_schedule:
            print("Tidak ada jadwal KA yang sesuai.")
            print()
            continue

        # Print semua jadwal kereta
        for sched in filtered_schedule:
            print(schedule_format.format(sched[0], sched[2], sched[3]))

    elif cmd == "EXIT":
        print("Terima kasih sudah menggunakan program ini!")
        break

    else:
        print("Perintah yang dimasukkan tidak valid.")
    print()
