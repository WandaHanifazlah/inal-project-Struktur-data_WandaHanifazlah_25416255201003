import csv
from collections import deque

FILE = "member.csv"

# Queue dan Stack
antrian = deque()
riwayat = []

# Membaca data dari CSV
def baca_data():
    data = []
    try:
        with open(FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data


# Menyimpan data ke CSV
def simpan_data(data):
    with open(FILE, mode="w", newline="") as file:
        fieldnames = ["id", "nama", "umur", "paket"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


# CREATE
def tambah_member():
    data = baca_data()

    id_member = input("ID Member : ")
    nama = input("Nama      : ")
    umur = input("Umur      : ")
    paket = input("Paket Gym : ")

    data.append({
        "id": id_member,
        "nama": nama,
        "umur": umur,
        "paket": paket
    })

    simpan_data(data)
    riwayat.append("Tambah " + nama)
    print("Member berhasil ditambahkan.")


# READ
def lihat_member():
    data = baca_data()

    if len(data) == 0:
        print("Belum ada data.")
        return

    print("\nDaftar Member")
    for m in data:
        print(m["id"], "-", m["nama"], "-", m["umur"], "tahun -", m["paket"])


# UPDATE
def update_member():
    data = baca_data()
    cari = input("Masukkan ID member: ")

    for m in data:
        if m["id"] == cari:
            m["nama"] = input("Nama baru : ")
            m["umur"] = input("Umur baru : ")
            m["paket"] = input("Paket baru: ")

            simpan_data(data)
            riwayat.append("Update " + cari)
            print("Data berhasil diupdate.")
            return

    print("Member tidak ditemukan.")


# DELETE
def hapus_member():
    data = baca_data()
    cari = input("Masukkan ID member: ")

    data_baru = [m for m in data if m["id"] != cari]

    if len(data) != len(data_baru):
        simpan_data(data_baru)
        riwayat.append("Hapus " + cari)
        print("Data berhasil dihapus.")
    else:
        print("Member tidak ditemukan.")


# SEARCHING
def cari_member():
    data = baca_data()
    cari = input("Masukkan ID member: ")

    for m in data:
        if m["id"] == cari:
            print("Data ditemukan:")
            print(m)
            return

    print("Member tidak ditemukan.")


# SORTING
def urutkan_member():
    data = baca_data()

    data.sort(key=lambda x: x["nama"])

    print("\nData setelah diurutkan:")
    for m in data:
        print(m["id"], "-", m["nama"])


# QUEUE
def tambah_antrian():
    nama = input("Nama member: ")
    antrian.append(nama)
    print("Masuk antrian trainer.")


def layani_antrian():
    if len(antrian) == 0:
        print("Antrian kosong.")
    else:
        print(antrian.popleft(), "sedang dilayani.")


# STACK
def lihat_riwayat():
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
    else:
        print("\nRiwayat Aktivitas:")
        for r in reversed(riwayat):
            print(r)


# MENU
while True:
    print("\n=== SISTEM MANAJEMEN KURSUS GYM ===")
    print("1. Tambah Member")
    print("2. Lihat Member")
    print("3. Update Member")
    print("4. Hapus Member")
    print("5. Cari Member")
    print("6. Urutkan Member")
    print("7. Tambah Antrian Trainer")
    print("8. Layani Antrian")
    print("9. Lihat Riwayat")
    print("10. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_member()
    elif pilihan == "2":
        lihat_member()
    elif pilihan == "3":
        update_member()
    elif pilihan == "4":
        hapus_member()
    elif pilihan == "5":
        cari_member()
    elif pilihan == "6":
        urutkan_member()
    elif pilihan == "7":
        tambah_antrian()
    elif pilihan == "8":
        layani_antrian()
    elif pilihan == "9":
        lihat_riwayat()
    elif pilihan == "10":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")