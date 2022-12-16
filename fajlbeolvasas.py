def beolvasas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='utf-8')
    print(fajlom)
    #fajltartalom = fajlom.read()
    #print(fajltartalom)
    fejlec = fajlom.readline().strip()
    print(fejlec)
    sorok = fajlom.readlines()
    print(sorok)
    fajlom.close()
    fajlfeldolgozas(sorok)


nevek = []
nemek = []
korok = []


def fajlfeldolgozas(sorok):
    i = 0
    while i < len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(", ")
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        i += 1
    print(nevek)
    print(nemek)
    print(korok)

def eletkor_atlag():
    i = 0
    eletkor_osszeg= 0
    db= 0
    while i < len(korok):
        eletkor_osszeg += korok[i]
        db += 1
        i += 1
    atlag = eletkor_osszeg / db
    print(f"Átlag életkor: {atlag}")

def adatok_sum():
    adatok_sum= len(nemek) + len(korok) + len(nevek)
    print(f"A fájlban összesen: {adatok_sum} db adat van rögzítve.")

def nok_mennyisege():
    i = 0
    nok_sum = 0
    while i < len(nemek):
        if nemek[i] == "nő":
            nok_sum += 1
        i += 1
    print(f"Összesen {nok_sum} darab nő van a listában.")

def legfiatalabb_no():
    i = 0
    legfiatalabb_no_eletkor = 120
    while i < len(nemek):
        if nemek[i] == "nő":
            if korok[i] < legfiatalabb_no_eletkor:
                legfiatalabb_no_eletkor = korok[i]
        i += 1
    print(f"A legfiatalabb nő életkora: {legfiatalabb_no_eletkor}")

def adatbekeres():
    nev = input("Add meg a neved: ")

    nem = input("Add meg a nemed: (n)ő/(f)érfi:  ")
    while nem != "nő" or nem != "férfi" or nem != "f" or nem != "f":
        nem = input("Add meg a nemed: (n)ő/(f)érfi:  ")

























