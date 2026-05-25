Hari ke-3 SELESAI

Link GitHub: https://github.com/Lukman-Hexa/Learn-Py/blob/master/Day3/task3.py

Waktu yang dihabiskan: 40 menit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ERROR LOG (wajib diisi): gua lupa
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(Kalau tidak ada error, tulis: "Tidak ada error berarti")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REFLEKSI:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Paling susah di bagian: mikin konsepnya gua rada rada bingun gua sebelumnya sempat mikir untuk buat varaiebl kesempatan sendiri.
Paling seru di bagian: yang paling seru ya kalau program jalan sebagai mana mestinya
Apakah bonus dikerjakan? (Lu bisa cek sendiri link github atau code di bawah.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROGRES LAINNYA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Main Minecraft hari ini: 30 menit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CEKLIST:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [DONE] Program tebak angka berjalan tanpa error
- [DONE] Fitur 3 kesempatan berfungsi
- [DONE] Feedback sesuai spesifikasi
- [DONE] Push ke GitHub sudah dilakukan
- [DONE] Spreadsheet task sudah dicentang

Wajib, lur! Jangan ada yang bolong.
Checklist ini biar lo ga kelewat.

#kode progamnya bre

import random

angka_rahasia = random.randint(1, 11)

for kesempatan in range(1, 4):
    tebak = int(input("tebak angka bre (1-10): "))
    sisa_kesempatan = 2 - (kesempatan - 1)

    if tebak > angka_rahasia:
        print(f"Kegedean, lek. Kesempatan lu {sisa_kesempatan}")
    elif tebak < angka_rahasia:
        print(f"Kekecilan, no!. Kesempatan lu {sisa_kesempatan}")
    else:
        print("good boy")
        break

else:
    print("Yah gagal. silahkan topup kembali")
