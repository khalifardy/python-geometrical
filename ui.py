from rumus import Lingkaran, Segitiga, Persegi, Persegi_panjang

def mulai():
        print("Assalamualaiku terima kasih sudah mau mencoba geometrical")
        pilihan = input("Anda ingin mencoba ? y=yes , n = no: ")

        while pilihan not in ["Y", "N", "y", "n"]:
            pilihan = input("Anda ingin mencoba ? y=yes , n = no: ") 

        if pilihan == "y" or pilihan == "Y" :
            menu()
         
        elif pilihan == "n" or pilihan == "N":
            print("terima kasih sudah mau mencoba")
            exit()

def menu():
        print("Apa yang anda butuhkan ? : ")
        print("1. Segitiga")
        print("2. Persegi")
        print("3. Persegi Panjang")
        print("4. Lingkaran" )
        pilihan2= int(input("silahkan memilih, 1,2,3,4 : "))

        while pilihan2 not in [1,2,3,4]:
           menu()

        if pilihan2 == 1 :
            segitiga()

        elif pilihan2 == 2 :
            persegi()

        elif pilihan2 == 3:
            persegipanjang()

        elif pilihan2 == 4:
            lingkaran()


def segitiga():
    print("anda ingin menghitung apa ? /n ?:"
          "1. Luas\n"
          "2. Keliling\n")
    pilihan3 = float(input("apa yang anda inginkan ?: "))

    while pilihan3 not in [1,2]:
        print("salah memasukan input")
        segitiga()

    if pilihan3 == 1 :
        alas = float(input("berapakah alasnya ? : "))
        tinggi = float(input("berapakah tingginy ? : "))
        print(Segitiga.luas(alas, tinggi))
    
    elif pilihan3 == 2:
        sisi1 = float(input("berapa nilai sisi1 ? : "))
        sisi2 = float(input("berapa nilai sisi2 ? : "))
        sisi3 = float(input("berapa nilai sisi3 ? : "))
        print(Segitiga.keliling(sisi1, sisi2, sisi3))


def persegi():
    print("anda ingin menghitung apa ? \n ?:"
          "1. Luas\n"
          "2. Keliling\n")
    pilihan4 = float(input("apa yang anda inginkan ?: "))

    while pilihan4 not in [1,2]:
        print("salah memasukan input")
        persegi()

    if pilihan4 == 1 :
        sisi = float(input("berapakah sisinya ? : "))
        print(Persegi.luas(sisi))
    
    elif pilihan4 == 2:
        sisi = float(input("berapa nilai sisinya ? : "))
        print(Persegi.keliling(sisi))

def persegipanjang():
    print("anda ingin menghitung apa ? \n ?:"
          "1. Luas\n"
          "2. Keliling\n")
    pilihan4 = float(input("apa yang anda inginkan ?: "))

    while pilihan4 not in [1,2]:
        print("salah memasukan input")
        persegipanjang()

    if pilihan4 == 1 :
        panjang = float(input("berapakah panjangnya ? : "))
        lebar = float(input("berapakah lebarnya ? : "))
        print(Persegi_panjang.luas(panjang, lebar))
    
    elif pilihan4 == 2:
        panjang = float(input("berapa nilai panjangnya ? : "))
        lebar = float(input("berapa nilai lebarnya ? : "))
        print(Persegi_panjang.keliling(panjang,lebar))

def lingkaran():
    print("anda ingin menghitung apa ? \n ?:"
          "1. Luas\n"
          "2. Keliling\n")
    pilihan5 = float(input("apa yang anda inginkan ?: "))

    while pilihan5 not in [1,2]:
        print("salah memasukan input")
        lingkaran()

    if pilihan5 == 1 :
        diameter = float(input("berapa nilai diameter ?: "))
        pilihan6 = input("apakah anda memiliki nilai jari-jari ? : ")

        while pilihan6 not in ["Y", "N", "y", "n"]:
            pilihan6 = input("apakah anda memiliki nilai jari-jari ? : ")
        
        if pilihan6 == "y" or pilihan6 == "Y":
            jari_jari = float(input("berapa nilai jari-jari ? :"))
            print(Lingkaran.luas(diameter, jari_jari))
        
        elif pilihan6 == "n" or pilihan6 == "N":
            print(Lingkaran.luas(diameter=diameter))
    
    elif pilihan5 == 2:
        diameter = float(input("berapa nilai diameter ?: "))
        pilihan7 = input("apakah anda memiliki nilai jari-jari ? : ")

        while pilihan7 not in ["Y", "N", "y", "n"]:
            pilihan7 = input("apakah anda memiliki nilai jari-jari ? : ")
        
        if pilihan7 == "y" or pilihan7 == "Y":
            jari_jari = float(input("berapa nilai jari-jari ? :"))
            print(Lingkaran.luas(diameter, jari_jari))
        
        elif pilihan7 == "n" or pilihan7 == "N":
            print(Lingkaran.luas(diameter=diameter))

mulai()