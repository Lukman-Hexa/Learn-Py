**Deklarasi & Aturan Penamaan**
pytho nmenggunakan dynamic typing tipe ditentukan otomatis saat runtime. Tidak perlu kata kunci seperti int atau var.

    nama = "Budi"   #str
    umur = 25       #int
    tinggi = 1.75   #float
    aktif = true    #boolean
    
    # Penugasan sekaligus (multiple assignment)
    x = y = z = 0
    
    # Tuple unpacking
    a, b, c = 1, 2, 3
    
    # swap tanpa variabel sementara
    a, b = b, a

**Gunakan huruf kapital + underscore untuk menandai konstanta. python tidak memiliki kata kunci const, namun konversi ini diikuti secara luas** 
#
**VARIABEL**
python menggunakan _dynamic typing_ tidaka perlu mendeklarasikan tipe secara eksplisit. Namun variable bersifat _case sensitive_, harus diawali huruf atau underscore, dan tidak boleh berupa reserved kyboard.
#
**TIPE DATA**
Pytho memiliki tipe data numerik (int, float, complex) teks (str), logika (bool), dan koleksi(list, tuple, dict, set). harus diketahui

- *int* di pythonn tidak memiliki batas ukuran (arbitrary precision)
- *bool* adalah subkelas dari *int* sehingga *True + True == 2*
- Nilai yang dianggap *false : 0, "",[], None*
- Gunakan *isinstance()* untuk mengecek tipe, bukan *type() ==*
#

    int("42")        # → 42
    float("3.14")    # → 3.14
    str(100)         # → "100"
    bool(0)          # → False  (0, "", [], {}, None → False)
    list((1,2,3))    # → [1, 2, 3]
    tuple([1,2,3])   # → (1, 2, 3)

#

    Tipe	    Contoh	              Keterangan
    int	      42,-7, 1_000_000	    Bilangan bulat, presisi tak terbatas
    float	    3.14, 2.0e8	          Bilangan desimal (64-bit IEEE 754)
    complex	  3+4j	                Bilangan kompleks
    str	      "halo", 'dunia'	      Teks immutable, Unicode penuh
    bool	    True, False	          Subkelas dari int (True=1, False=0)
    list	    [1, 2, 3]	            Urutan mutable, bisa campur tipe
    tuple	    (1, 2, 3)	            Urutan immutable
    dict	    {"a": 1}	            Pasangan kunci-nilai, urutan terjaga (3.7+)
    set	      {1, 2, 3}	            Himpunan, tanpa duplikat, tidak terurut
    NoneType	None	                Mewakili "tidak ada nilai"

**OPERATOR**
selain operator standar, python punya beberapa yang unik: *//* untuk _floor division_,** untuk pangkat, dan *is* untuk perbandingan identitas objek (berbeda dengan *==* yang membandingkan nilai). Walrus operator (:=) memungkinkan penugasan sekaligus evaluasi dalam satu ekspresi.
#
**INPUT/OUTPUT**
Fungsi *input()* selalu mengembalikan *str*, jika konversi tipe wajib dilakukan secara manual. unutk membaca banyak angka sekaligus, pola *map(int, input().split())* sangat umum dipakai di competitive programing maupun scripting.
#
**F-STRING**
F-String adalah cara terformart terbaik di Python modern. beberapa fitur penting:
- *Format spec* mengikuti pola *{nilai:lebar.presisi_tipe}*, misal *{pi:.2f}*
- *Debug mode* *{x = }* sangat berguna saat debugging langsung menampilkan nama variabel dan nilainya.
