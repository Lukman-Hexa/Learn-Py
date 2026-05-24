**IMPORT RANDOM**
menghasilan nilai acak semu, artinya hasil sebenarnya di hitung pakai rumus matematis yang kompleks, bukan benar-benar 'acak abolut' dari alam. Tapi buah 99% keperluan porgramming (game, simulasi, sampling, resting)

*random.uniform(a, b)*

    print(random.uniform(1.5, 9.5)) # float antara 1.5 dan 9.5

*random.choice(seq)*

    menu = ["Nasi Goreng", "Mie Ayam", "Soto"]
    print(random.choice(menu)) # Bakso dll

*random.shuffle(list)*

    kartu = ["A", "K", "Q", "j", "10"]
    random.shuffle(kartu) # modifikasi di tempat (in-place)
    print(kartu)

*random.sample(seq, k)*
    
    peserta = ["Andi", "Budi", "Bapak Andi", "Bapak Budi"]
    print(random.sample(peserta, 3)) # 3 pemenang tanpa duplikat

*random.seed*

    random.seed(42)
    print(random.radiant(1, 100)) # selalu sama: 82
    random.seed(42)
    print(random.radiant(1, 100)) # tetap 82 sama persis
