import random
lista = []
def sorozat_():
    i = 0
    dollar = ""
    while (i <= 11):
        vel = int(random.random() * 1011) - 10
        lista.append(vel)
        if (i == 11):
            dollar += str(vel) + ""
        else:
            dollar += str(vel) + "$"
        i += 1
    print(f" II/A, B, C: \n \t {dollar}")


def paratlan_szamok():
    i = 0
    paratlan_darab = 0

    while i < len(lista):
        if (lista[i] % 2) != 0:
            paratlan_darab += 1
        i += 1
    return paratlan_darab


def konzol_kiir():
    print(f" II/D, E: \n \t A páratlanok száma: {paratlan_szamok()}")


def fajlba_kiir():
    fajl = open("eredmeny.txt", "w", encoding="utf-8")
    fajl.write(f"II/F: \n \t A páratlanok száma: {str(paratlan_szamok())}")
    fajl.close()
    print(fajl)


