import typing as t

print("Masukkan rantai penyebaran:")

infection_data: t.Dict[str, t.Set[str]] = {}

while True:
    infection = input()
    if infection == "selesai":
        break

    splitted_data = infection.split()
    infector, infecteds_list = splitted_data[0], splitted_data[1:]

    # Apabila penular tidak ada di dalam dict, maka buat entry untuk
    # penular tersebut dengan empty set.
    if infector not in infection_data:
        infection_data[infector] = set()

    infection_data[infector].update(infecteds_list)


def get_infections(source: str) -> t.Set[str]:
    """Ambil semua orang yang tertular secara langsung
    dan tidak langsung oleh source."""
    # Return empty set apabila source tidak ada dalam
    # data infeksi
    if source not in infection_data:
        return set()

    # Copy agar tidak memodifikasi dict
    infected = infection_data[source].copy()

    # Apabila tidak menular ke siapa-siapa, maka return set dengan diri sendiri
    if not infected:
        return {source}

    # Rekursi fungsi untuk semua orang yang tertular
    # Copy agar hanya iterasi pada original
    for person in infected.copy():
        infected.update(get_infections(person))
    infected.add(source)

    return infected


print()
print("List perintah:")
print("1. RANTAI_PENYEBARAN")
print("2. CEK_PENULARAN")
print("3. EXIT")

while True:
    print()
    command = input("Masukkan perintah: ").split()
    cmd_name, args = command[0], command[1:]

    if cmd_name == "RANTAI_PENYEBARAN":
        infector = args[0]
        # Orang tidak ada dalam data infeksi
        if infector not in infection_data:
            print(f"Maaf, nama {infector} tidak ada dalam rantai penyebaran.")
            continue

        infecteds = get_infections(infector)
        print(f"Rantai penyebaran {infector}:")
        for person_infected in infecteds:
            print("-", person_infected)

    elif cmd_name == "CEK_PENULARAN":
        invalid_names = set()
        # Cari orang-orang yang tidak ada di dalam data infeksi
        for name in args:
            if name not in infection_data:
                invalid_names.add(name)

        # Terdapat orang yang tidak valid dalam argumen
        if invalid_names:
            names = " dan ".join(invalid_names)
            print(f"Maaf, nama {names} tidak ada dalam rantai penyebaran.")
            continue

        infected, infector = args
        # Cek apakah orang berada dalam rantai penyebaran infector
        if infected in get_infections(infector):
            print("YA")
        else:
            print("TIDAK")

    elif cmd_name == "EXIT":
        print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
        break

    else:
        print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")
