nama = input("masukkan nama anda: ")
umur = input("masukkan umur anda: ")
umur = int(umur)
"""
V2
umur = int(input("masukan umur: ))

langsung merubaha manual yang dimna sebelumnya semua type data input
string menajdi interger
"""
kota = input("Masukkan adalah kota anda: ")
tahun = 2026 - umur
tahun5 = umur + 5

print(f"Halo, saya {nama}. Umur saya {umur} tahun. Saya tinggal di {kota}")
print(f"{nama} Lahir tahun {tahun}")
print(f"Umur {nama} lima tahun kedepan umurnya {tahun5}")
print(type(nama))
print(type(umur))
print(type(kota))
print(type(tahun))
