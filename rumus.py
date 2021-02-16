import math

class Segitiga(object):
    def luas(alas,tinggi):
        return alas * tinggi/2

    def keliling(sisi1,sisi2,sisi3):
        return sisi1+sisi2+sisi3

class Persegi(object):
    def luas(sisi):
        return sisi ** 2

    def keliling(sisi):
        return 4 * sisi

class Lingkaran(object):
    def luas(diameter=0, jari_jari=0):
        if diameter != 0 and jari_jari == 0 :
            return math.pi * diameter**2 / 4

        elif diameter==0 and jari_jari !=0:
            return math.pi * jari_jari**2 

        elif diameter == 0 and jari_jari == 0:
            return 'diameter atau jari-jari belum terisi'

        else:
            return math.pi * jari_jari**2

    def keliling(diameter=0, jari_jari = 0):
        if diameter != 0 and jari_jari == 0 :
            return math.pi * diameter

        elif diameter==0 and jari_jari !=0:
            return math.pi * 2 * jari_jari  

        elif diameter == 0 and jari_jari == 0:
            return 'diameter atau jari-jari belum terisi'

        else:
            return math.pi * jari_jari *2

class Persegi_panjang (object):
    def luas(panjang,lebar):
        return panjang * lebar

    def keliling(panjang,lebar):
        return 2 * (panjang + lebar)

