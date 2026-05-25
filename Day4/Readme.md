# **DEF (Fungsi)**

### **Apa itu Fungsi? Kenapa dibutuhkan?**
---
>Bayangkan km bekerja di dapur restoran. Setiap hari kamu membuat nasi goreng dengan langkah yang sma persis: panaskan wajan, masukkan bumbu, masukkan nasi, aduk, dan sajikan. Dari pada menghapal ulang langkah itu setiap hari, kamu cukup bilang:"Buat nasi goreng!" dan semua langkah berjalan otomatis.

### **Fungsi dalam python bekerja persis seperti itu.**
---
***Fungsi adalah block kode yang diberi nama***,yang > bisa di panggil berulang kali tanpa menulis ualng kodenya. Tiga alasan utama kenapa fungsi itu penting.

  1. Reusabilit : Tulis sekali, pakai berkali-kali.
  2. Modularity : Pisahkan masalah besar mennjadi bagian kecil
  3. Readability : kode lebih mudah dibaca dan dipahami.
---

**TANPA** fungsi - kode berulang terus

    print("selamat datang, User1")
    print("selamat datang, User2")

**DENGAN FUNGSI** tulis sekali, pakai berkali-kali

    def sambut(nama):
      print("Selamat datang, {nama}")

    sambut("User3")

## **Cara Membuat Fungsi**
---
    def nama_fungsi(parameter):
        # isi kode (wajib di-indentasi)
        # ...
**Tiga aturan penting:**
1. Kata kunci `def` wajib, artinya "definisikan fungsi ini"
2. Penamaan `snake_case` semua huruf kecil, kata dipisah underscore `_`.

**BENAR**

    def hitung_luas()
    def cek_nilai_siswa()
**SALAH**

    def HitungLuas()
    def hitungLuas()
    def hitung luas()

3. Identasi isi fungsi wajib menjorok ke dalam (4 spasi/1tab)
#
    def sapa_dunia():
      print("Hello World")  # didalam fungsi
      print("Apa Kabar?")   # masih di dalam fungsi
    print("ini di luar fungsi")   # ini di luar fungsi (tidak identasi)

## **Parameter vs Argumen**
---
analogi sederhana:
- **Parameter** = slot kosong di menu restoran:"Ukuran pizza"
- **Argument** = isian yang kamu tulis:"Ukuran piza: Large"
#
    "nama" dan "umur" adalah PARAMETER placeholder saat fungsi dibuat
    
    def perkenalan(nama, umur):
      print(f"Nama saya {nama}, umur {umur} tahun")
    
    "Budi" dan 20 adalah ARGUMEN nilai nyata fungsi dipanggil
    
    perkenalan("Budi", 20)
    perkenalan("Admin", 22)

intinya:
* Parameter -> ada di definisi fungsi (`def`)
* Argument -> ada saat panggilan fungsi

## **Return Value vs Print Bedanya Saat Penting**
konsep yang harus di pahami untuk backend
Analoginya:
* print = Kalkulator yang hanya menampilkan angka di layar, tapi hasilnya tidak bisa kamu simpan atau pakai lagi.
* return = kalkulator yang menyerahkan hasilnya ke tanganmu km bisa simpan, kirim ke fungsi lain, atau proses lebih lanjut.
#
    Fungsi dengan **PRINT** hasilnya tampil tapi tidak bisa di pakai 
    def tambah_print(a, b):
      print(a + b)
    
    hasil = tambah_print(3, 5)  # tampil: 8
    print(hasil)                # Tampil: None
    
    Fungsi dengan **RETURN** hasilnya bisa disimpan dan dipakai
    
    def tambah_return(a, b):
      print(a + b)
    
    hasil = tambah_return(3, 5)  # tidak tampil apa"
    print(hasil)                 # Tampil: 8
    print(hasil * 2)             # Tampil: 16

Kapan pakai `print` vs `return`?
* Hanya ingin tampilkan ke layar `print`
* Hasil akan dipakai kode lain `return`
* Membuat fitur backend/API `return`(hampir selalu)
* Debuggint cepat `print`

## **Memanggil Fungsi & Menyimpan Hasil Return**

    def hitung_luas_persegi(sisi):
      luas = sisi * sisi
      return luas
    
    Cara 1: simpan dulu, pakai nanti
    luas_kamar = hitung_luas_persegi(5)
    print(f"Luas kamar: {luas_kamar} M2") # 25m2
    
    Cara 2: Langsung pakai tanpa disimpan
    print(hitung_luas_persegi(10)) # 100
    
    Cara 3: Pakai hasil sebagai argumen fungsi lain
    print(f"Luas: {hitung_luas_persegi(7)} m2") # Luas: 49 m2
    
    Cara 4: Gunakan hasil untuk perhitungan lanjutan
    luas_a = hitung_luas_persegi(4)
    luas_b = hitung_luas_persegi(6)
    total = luas_a * luas_b
    print(f"Total luas: {total} m2") # Total luas: 52 m2

## **Scope Variabel Lokal vs Global**

Scope = "wilayah berlakunya" sebuah variabel.

Analoginya seperti aturan di gedung kantor:
> **Variabel Global** = papan pengumuman di lobay sebuah orang di seluruh gedung bisa membacanya. **Variabel Lokal** = catatan di meja kerja km hanya km (fungsi itu) yang bisa akses. orang laint daik bisa masuk dan membacanya.

    VARIABEL GLOBAL dibuat di luar fungsi
    
    nama_app = "TokoU"
    
    def tampilkan_info():
      VARIABEL LOKAL hanya hidup di dalam fungsi ini
      versi = "1.0"
      print(f"App: {nama_app}") # bisa akses variabel global
      print(f"Versi: {versi}")  # bisa akses variabel lokal sendiri
    
    tampilkan_info()
    print(nama_app) # bisa Variabel Global
    print(versi) # tidak bisa Variabel Lokal

**Hati-hari mengubah variabel global dari dalam fungsi:**

    stok = 10
    
    def kurangi_stok():
        stok = stok - 1   # ❌ ERROR! Python bingung: ini lokal atau global?
    
    def kurangi_stok_benar():
        global stok        # ✅ beritahu Python: pakai yang global
        stok = stok - 1
    
    kurangi_stok_benar()
    print(stok)  # 9

**`⚠️ Tips Backend: Di dunia nyata, sebaiknya hindari mengubah variabel global langsung. Lebih baik kirim nilai lewat parameter dan kembalikan lewat return. Kode jadi lebih aman dan mudah di-debug.`**

    # ============================================================
    # CARA BURUK ❌ — fungsi bergantung pada variabel luar
    # ============================================================
    diskon = 20  # global
    
    def hitung_harga_buruk(harga):
        global diskon
        return harga - (harga * diskon / 100)
    
    # Suatu hari ada kode lain yang tidak sengaja ubah diskon:
    diskon = 0   # ← diubah di tempat lain dalam program
    
    print(hitung_harga_buruk(100000))  # → 100000, diskon tidak jalan! 😱
    # Kamu bingung kenapa hasilnya salah, padahal fungsinya terlihat benar
    
    
    # ============================================================
    # CARA BENAR ✅ — semua nilai masuk lewat parameter
    # ============================================================
    def hitung_harga_benar(harga, diskon):
        return harga - (harga * diskon / 100)
    
    print(hitung_harga_benar(100000, 20))  # → 80000.0, selalu benar ✅
    print(hitung_harga_benar(100000, 0))   # → 100000.0, jelas dan terprediksi ✅


## **Contoh Lengkap 4 Jenis Fungsi**
1. Fungsi Tanpa Parameter
#
    def tampilkan_garis():
      print(f""+" * 30)

    tampilkan_garis()
    LAPORAN
    tampilkan_garis()
    
    Output:
    =======================
    LAPORAN 
    =======================
    
2. Fungsi Dengan Parameter
#
    def sapa_pengguna (nama, kota):
      print(f"Hola {nama}, dari mna {kota}")
    
    sapa_pengguna("Budi", "Isekai")
    
    Output:
    Hola Budi, dari mna Isekai

3. Fungsi Dengan Return
#
    def hitung_diskon(harga, persen_diskon):
        diskon     = harga * (persen_diskon / 100)
        harga_akhir = harga - diskon
        return harga_akhir
    
    harga_baju  = hitung_diskon(150000, 20)  # diskon 20%
    harga_sepatu = hitung_diskon(300000, 30) # diskon 30%
    
    print(f"Harga baju setelah diskon : Rp{harga_baju:,.0f}")
    print(f"Harga sepatu setelah diskon: Rp{harga_sepatu:,.0f}")
    print(f"Total belanja              : Rp{harga_baju + harga_sepatu:,.0f}")
    
    Output:
    Harga baju setelah diskon : Rp120,000
    Harga sepatu setelah diskon: Rp210,000
    Total belanja              : Rp330,000

4. Fungsi Tanpa Retrun (mengambalikan `None`)
#
    def catat_log(pesan):
        print(f"[LOG] {pesan}")
        # tidak ada return → otomatis return None
    
    catat_log("Pengguna berhasil login")
    catat_log("Data berhasil disimpan")
    
    hasil = catat_log("Test")
    print(hasil)  # None — tidak ada nilai yang dikembalikan

### **Kesimpulan: Kapan Sebaiknya Kita Membuat Fungsi?**
Buat fungsi ketika kamu menemukan salah satu kondisi ini:
* 🔁 Kode diulang 2x atau lebih Jika kamu menulis blok kode yang sama lebih dari sekali → buat fungsi.
* 📦 Ada tugas yang jelas batasannya "Hitung diskon", "Validasi email", "Kirim notifikasi" → satu tugas = satu fungsi.
* 🧩 Kode terlalu panjang dan susah dibaca Jika satu file sudah ratusan baris tanpa fungsi → pecah jadi fungsi-fungsi kecil.
* 🔧 Kode kemungkinan akan berubah Jika logika diskon berubah, lebih mudah ubah di satu fungsi daripada mencari di 20 tempat.
#
    Contoh nyata untuk backend sederhana
    def validasi_umur(umur):
        return umur >= 17
    
    def hitung_total(harga, jumlah):
        return harga * jumlah
    
    def format_rupiah(nominal):
        return f"Rp{nominal:,.0f}"
    
    Gunakan semua fungsi di atas secara terorganisir
    umur_pembeli = 20
    harga_tiket  = 50000
    jumlah_tiket = 3
    
    if validasi_umur(umur_pembeli):
        total = hitung_total(harga_tiket, jumlah_tiket)
        print(f"Total pembayaran: {format_rupiah(total)}")
    else:
        print("Maaf, kamu belum cukup umur.")
    
    Output :
    Total pembayaran: Rp150,000

### **Contoh Nyata Nested Function**
    def hitung_belanja(daftar_harga, persen_diskon):
    
        # Fungsi dalam — helper khusus untuk tugas ini
        def terapkan_diskon(harga):
            return harga - (harga * persen_diskon / 100)
    
        total = 0
        for harga in daftar_harga:
            harga_diskon = terapkan_diskon(harga)  # pakai fungsi dalam
            total += harga_diskon
    
        return total
    
    belanjaan = [50000, 120000, 80000]
    hasil = hitung_belanja(belanjaan, 10)  # diskon 10%
    print(f"Total bayar: Rp{hasil:,.0f}")
