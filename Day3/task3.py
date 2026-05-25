import random

while True:
    angka_rahasia = random.randint(1, 10)
    skor = int()
    for kesempatan in range(1, 4):
        tebak = int(input("tebak angka bre (1-10): "))
        sisa_kesempatan = 3 - kesempatan

        if tebak > angka_rahasia:
            print(f"Kegedean, lek. Kesempatan lu {sisa_kesempatan}")
        elif tebak < angka_rahasia:
            print(f"Kekecilan, no!. Kesempatan lu {sisa_kesempatan}")
        else:
            print("good boy", skor + 10)
            print(f"Skor Lu Sekarang: {skor}")
            break
    else:
        print("Yah gagal. silahkan topup kembali")

    main_lagi = input("Main Lagi (y/n) ")
    if main_lagi != "y":
        break
