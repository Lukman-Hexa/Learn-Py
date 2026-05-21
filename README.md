**Python**

    - Buat Venv -
    python -m venv (nama_venv)
    - Aktifkan Venv -
    source (nama_venv)/bin/activate

Abstraksi merupakan kemampuan untuk mengerti konteks dan merepresentasikannya menjadi bentuk lain dengan konteks masalahnya.
Python menerapkan **loosley typed** artinya tidak perlu mendeklarasikan tipe data variabel secara eksplisit. Python merupakan bahasa pemrograman yang menerapkan **dynamic typing** artiya python bhs pemrograman yang hanya mengetahui tipe variabel saat program berjalan dan melakukan proses assignment. **string** pada py bersifat *immutable* yang artinya tidak dpt diubah.

**Pengertain Ekspresi** (Syntax yang dapat di evaluasi ke beberapa nilai) pada matematika dalam pemrograman **Ekspresi** merupakan kombinasi dari suatu atau lebih variabel, konstatant, oerator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu. Ekpresi yang sering dijumpai adalah <operan1><operator><operan2> itu merupakan struktur biner (jenis ekspresi menggunakan dua operan).

Jenis Jenis Ekspresi Menurut Arity dari Operator

    Bine = 
    (x + y)
    (x - y)
    (x \* y)
    (x / y)
    (x \*\* y)
    (x < y)
    (x <= y)
    (x > y)
    (x >= y)
    (x % y)
    (x == y)
    (x != y)

**Case sensitive** python memperlakukan huruf besar dan kecil sebagai karakter yang berbeda dalam penaaam variabel.

**One-liner** untuk membuat satu baris kdoe yang singkat dan jelas. yang dimna one-liner merupakan gaya penulisan pada python yang memungkinkan untuk membuat sebuah kode hanya dalam satu baris.

**Aksi sekuensial** adalah sederetan instruktri yang akan dijalankan oleh komputer berdasarkan uturan penulisannya.

**Control flow** adalah sebuah cara untuk memberi tahu program mengeni instruksi yang harus dijalnkan dan di mana harus memulai dan berakhir, control flow terbagi menjadi beberapa jenis yakni kondisi tertentu (percabangan), mengulan block kode secara berulang (perulangan), melewati sebagai kode dan berhenti di kode tertentu hingga mendefinisikan fungsi.

**If**  adalah statement python yang akan mencetak nilai variabel di dalamnya memenuhi kriteria satu kondisi atau tidak.

**Else** adalah statement yang menjadi jalan keluar saat kondisi atau hasil evaluasi **if** statement.
**Elif** merupakan kependekan dari **else if** dan alternatif untuk if bertingkat atau switch case Elif statement berada pada posisi setelah if.

**Ternary operators** merupakan **Conditional expressions** adalah bentuk ekspresi (syntax yang dapat di evaluasi ke beberapa nilai) yang bertujuan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya.

**For** termasuk sintaks dalam python yang bersifat **definite iteration** iadalah sebuah proses iterasi atau perulangan ketika jumlah perlangannya ditentukan secara eksplisit sebelumnya. 

        "Sintaksi *range() =* range(start, stop, step)"

**While** termasuk sintaks dalam python yang bersifat **idefinite iteration** adalah sebuah proses iterasi yang akan berhenti ketika memnuhi kondisi tertentu. **Increment** adalah pola untuk menambahkan suatu varaibel dengan nilai tetap.

                counter = 1
                while counter <= 10: #kondisi
                    print(counter)
                    counter += 1 # increment

increment adalah pola untuk menambahkan suatu variabel dengan nilai tetap. pada contoh di atas, `counter += 1` adalah increment yang menambahkan `counter` dengan nilai `1` setiap kali perulangan berlanjut. oke

Perulangan dalam perulangan disebut sebagai **nested loop.**

**Break**  pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut dan kemudian dilanjutkan mengeksekusi blok perulangan selanjutnya jika memiliki perulangan yang bertingkat.

      for huruf in 'Wiwok de tok':
          if huruf == ' ':
              break
          print('Huruf saat ini' {}'.format(huruf))

      #Output:
      Huruf saat ini: W
      Huruf saat ini: i
      Huruf saat ini: w
      Huruf saat ini: o
      Huruf saat ini: k
      
**Continue** pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. continue seolah mengabaikan pernyataan (statement) yang berada diantara continue hingga akhir block.

      for huruf in 'Wiwok de tok':
          if huruf == ' ':
              continue
          print('Huruf saat ini: {}'.format(huruf))
      
      Output:
      Huruf saat ini: W
      Huruf saat ini: i
      Huruf saat ini: w
      Huruf saat ini: o
      Huruf saat ini: k
      Huruf saat ini: d
      Huruf saat ini: e
      Huruf saat ini: t
      Huruf saat ini: o
      Huruf saat ini: k

**Else setalah for** berfungsi untuk perulangan bersifat pencarain. Else setalh for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.

      numbers = [1, 2, 3, 4, 5]
      
      for num in numbers:
          if num == 6:
              print('Angka ditemukan program berhenti')
              break
      else:
          print('Angka tidak ditemukan.')
      
      Output:
      Angka tidak ditemukan.

**Else Setalah While** else setalah while akan selalu dieksekusi saat kondisi pada while menjadi salah

      count = 0
      while count < 5:
          print("Pertamina Indo")
          count += 1
      else:
          print("Count sudah mencapai 5")
      
      # Output :
      Pertamina Indo
      Pertamina Indo
      Pertamina Indo
      Pertamina Indo
      Pertamina Indo
      Count sudah mencapai 5

Jika menggunakan **break** :

    n = 10
    while n > 0:
        n = n - 1
        print(n)
        if n == 5:
            break
        print(n)
    else:
        print('Loop selesai')
    
    #Output:
    9
    8
    7
    6
    Loop selesai

**Pass**
Pass statement adalah pernyataan yang digunakan jika menginginkan sebuah pernyataan atau block pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apapun.

    x = 10
    
    if x > 5:
        pass
    else:
        print("nilai x tidak memenuhi kondisi")
    
    #Output:

tidak ada hasil output apapun dikarenakan jika kondisi terpenuhi program tidak akan melakukan apapun statement pass dapat digunakan dalam situasi ketika python memerlukan adanya pernyataan, tetapi tidak memiliki tindakan yang perlu dilakukan pada saat itu. biasanya itu adalah kondisi ketika membutuhkan _placeholder_ untuk menunjukan bahwa tidak ada operasi yang perlu dilakukan. hal tersebut dapat membantu dalam mengatur struktur kode secara rapi dan memungkinkan penambahan implementasi di kemudian hari.

**List Comprehension**
masi terkait dengan perulangan terkadang ada kalanya perlu membuat sebuah list baru berdasarkan list yang sudah ada.

**Contoh dalam perulangan:**

    # Versi 1
    angka = [1, 2, 3, 4]
    pangkat = []
    
    for n in angka:
      pangkat.append(n**2)
    print(pangkat)
    
    #Output:
    [1, 4, 9, 16]

    # Versi 2
    angka = [1, 2, 3, 4]
    pangkat = [n**2 for n in angka]
    print(pangkat)

    #Output:
    [1, 4, 9, 16]
    
    
**Contoh lainnya :**

    # Contoh 1
    kuadrat = [i**2 for i in range(10)]
    #         └───── LIST COMPREHENSION ────┘ 
    
    # Contoh 2  
    genap = [i for i in range(1, 11) if i % 2 == 0]
    #       └────────── LIST COMPREHENSION ───────────┘
    
    # Contoh 3
    nama_besar = [n.upper() for n in nama]
    #            └─ LIST COMPREHENSION ──┘
    
    # Contoh 4
    hasil = ['ganjil' if i % 2 != 0 else i for i in range(10)]
    #        └──────────────── LIST COMPREHENSION ────────────────┘
    
    # Contoh 5
    gabungan = [w + ' ' + u for w in warna for u in ukuran]
    #           └────────── LIST COMPREHENSION ───────────┘

jadi list comprehension merupakan sebuah cara untuk menghasilkan list baru berdasarkan list atau iterable yang telah ada sebelumnya. sintaks dasarnya adalah:

    new_list=[expression for_loop_one_or_more_conditons]
