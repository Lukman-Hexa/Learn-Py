Hari ke-4 - LAPORAN

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CEK PEMAHAMAN (Jawab Ya/Tidak):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Bikin fungsi dari nol tanpa lihat contoh: Ya
2. Paham beda parameter dan argumen: ya
3. Paham beda return dan print: ya
4. Paham fungsi bisa manggil fungsi lain: ya
5. Paham variabel lokal vs global: ya
6. Bisa bikin default parameter: ya
7. Paham beda fungsi pake return vs tidak: kurang yakin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FITUR YANG UDAH BISA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Semua penjumlahan
- Untuk nilai nol tidak dapat di bagi
- Pilihan untuk mulai lgi (y/n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FITUR YANG BELUM BISA / MASIH BINGUNG:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- bisa di bilang bisa dan tidak untuk yg nol soalnya beda untuk implementasinya gua mikir gini lebih gampang
- tampilan gua bisa aja sebenarnya tinggal buat fungsi tampil terus hasil yg di tampl tadi gua masukin aja ke dalam fungsi dan tinggal panggil fungsi tersebut ketika user selesai isi inputan angka

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ERROR YANG MUNCUL (kalau ada):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- "break" can be used only within a loop
- Hasil pengurangan 4 - 2 = <function kurang at 0x00000203577EF760>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YANG UDAH DICOBA TAPI GAGAL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Di bagian untuk validasi nilai 0 yang tidak seharusnya tapi gua akalin biar bisa cuman tidak di fungsi bagi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WAKTU YANG DIHABISKAN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
60 menit kurang lebih

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KODE PROGRAM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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
