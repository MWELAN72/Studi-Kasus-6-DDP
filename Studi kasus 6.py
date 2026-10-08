import json

nama_file = "data_barang.json"


def baca_data():
    try:
        with open(nama_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def tampilkan_data():
    data_barang = baca_data()

    print("\n=== daftar inventaris barang ===")

    if len(data_barang) == 0:
        print("Belum ada data barang.")
    else:
        print("-" * 50)
        print(f"{'No':<5}{'Nama Barang':<20}{'Stok':<10}{'Satuan':<10}")
        print("-" * 50)

        for i, barang in enumerate(data_barang, start=1):
            print(
                f"{i:<5}"
                f"{barang['nama']:<20}"
                f"{barang['stok']:<10}"
                f"{barang['satuan']:<10}"
            )

        print("-" * 50)


def tambah_data():
    data_barang = baca_data()

    print("\n=== tambah data barang ===")

    nama = input("Nama barang : ")
    satuan = input("Satuan      : ")

    while True:
        try:
            stok = int(input("Jumlah stok : "))

            if stok < 0:
                print("Stok tidak boleh negatif.")
            else:
                break

        except ValueError:
            print("Stok harus berupa angka.")


    barang_baru = {
        "nama": nama,
        "stok": stok,
        "satuan": satuan
    }

    data_barang.append(barang_baru)

    with open(nama_file, "w") as f:
        json.dump(data_barang, f, indent=4)

    print("Data barang berhasil ditambahkan dan disimpan.")


while True:
    print("\n=== Sistem manajemen inventaris barang ===")
    print("1. Lihat data barang")
    print("2. Tambah data barang")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        tambah_data()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")