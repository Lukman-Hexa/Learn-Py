def catat_log(pesan):
        print(f"[LOG] {pesan}")
        # tidak ada return → otomatis return None

    catat_log("Pengguna berhasil login")
    catat_log("Data berhasil disimpan")

hasil = catat_log("Test")
print(hasil)  # None — tidak ada nilai yang dikembalikan
