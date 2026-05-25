def tambah(a, b):
    penjumlahan = a + b
    return penjumlahan


def kurang(a, b):
    # mengembalikan hasil a - b
    pengurangan = a - b
    return pengurangan


def kali(a, b):
    # mengembalikan hasil a * b
    perkalian = a * b
    return perkalian


def bagi(a, b):
    pembagian = a / b
    return pembagian

    # Opsi 2
    # if b == 0:
    #     return "Error: Tidak bisa dibagi nol!"
    # return a / b


while True:
    a = int(input("Masukkan Angka Pertama: "))
    b = int(input("Masukkan Angka Kedua: "))

    print("====================================")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("====================================")
    operator = int(input("Pilih Operator Berdasarkan Angka: "))
    if operator not in [1, 2, 3, 4]:
        print("Pilihan tidak valid! Pilih 1-4.")
        continue  # ulang loop tanpa ngitung ulang
    if operator == 1:
        hasil = tambah(a, b)
        print(f"Hasil penjumlahan {a} + {b} = {hasil}")
    elif operator == 2:
        hasil = kurang(a, b)
        print(f"Hasil pengurangan {a} - {b} = {hasil}")
    elif operator == 3:
        hasil = kali(a, b)
        print(f"Hasil perkalian {a} * {b} = {hasil}")
    else:
        if operator == 4 and b == 0:
            print("Error: Tidak bisa dibagi nol!")
            continue
        hasil = bagi(a, b)
        print(f"Hasil pembagian {a} / {b} = {hasil}")

    hitung_lagi = input("Main Lagi (y/n) ")
    if hitung_lagi != "y":
        break
