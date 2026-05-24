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
