**Task yang harus diselesaikan :**

    1. program punya angka rahasia (boleh tentukan manual dulu misal 7)
    2. user diminta tebak angka
    3. feedback sesuai tebakan :
        - tebakan > angka rahasia ->"kgedean, bro!"
        - tebakan < angka rahasia ->"kekecilan, bro!"
        - tebakan = angka rahasia ->"Bener! Lu hebat!"
    4. maksimal 3 kesempatan
    5. Setiap salah, kasih tau sisa kesemmpatan
    6. kalau 3 kali salah -> tampilin angka rahasia Exp="Yah ggl, angka rahasianya adalah 7"
    7. kalau tebakan benar dalam <3kali -> program selesai (tidak di minta tebak lagi)
#
**Skenario 1: Menang**

    Tebak angka (1-10): 5
    Kekecilan, bro! Sisa kesempatan: 2
    
    Tebak angka (1-10): 8
    Kegedean, bro! Sisa kesempatan: 1
    
    Tebak angka (1-10): 7
    Bener! Lu hebat!

**Skenario 2: Kalah**

    Tebak angka (1-10): 2
    Kekecilan, bro! Sisa kesempatan: 2
    
    Tebak angka (1-10): 9
    Kegedean, bro! Sisa kesempatan: 1
    
    Tebak angka (1-10): 5
    Kekecilan, bro! Sisa kesempatan: 0
    
    Yah gagal. Angka rahasianya adalah 7

**🎁 Bonus (Kalau Selesai Cepat)**

      Bonus	Tingkat Kesulitan	Point
      A. Angka rahasia acak setiap program dijalankan 
      (pakai random.randint())	
      ⭐⭐	+1
      
      B. Fitur "Main lagi?" setelah menang/kalah (y/n),
      kalau y → ulang dari awal	
      ⭐⭐⭐	+2
      
      C. Simpan skor (berapa kali menang dari total main)
      selama program berjalan	
      ⭐⭐⭐⭐	+3
