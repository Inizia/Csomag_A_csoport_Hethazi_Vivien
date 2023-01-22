from Pogyasz import Pogyasz

csomag_lista = []
def beolvas():
    csomag_fajl = open("csomag.txt", "r", encoding="utf-8")
    csomag_fajl.readline()
    csom = csomag_fajl.readlines()
    csomag_fajl.close()

    print(csom)
    i = 0
    while i < len(csom):
        ertek = csom[i].strip().split("#")
        csomag_lista.append(Pogyasz(ertek))
        i += 1

def pogyaszok_szama():
    print(f" III/A, B: \n \t A pogyászok száma: {len(csomag_lista)}")


def otvenegyesek_atlagszel():
    i = 0
    darab = 0
    atlagsuly = 0
    while i < len(csomag_lista):
        if csomag_lista[i].szelesseg == 51:
            darab += 1
            atlagsuly += csomag_lista[i].suly
        i += 1
    atlag = atlagsuly / darab
    print(f"III/C: \n \t Az 51 cm-es pogyászok átlag súlyértéke: {atlag * 1000} g")


def legmagasabb():
    i = 0
    magas = csomag_lista[0]
    while i < len(csomag_lista):
        if csomag_lista[i].magassag > magas.magassag:
            magas = csomag_lista[i]
        i += 1
    print(f" III/D: \n \t A legmagasabb pogyász méretei: {magas.szelesseg}x{magas.magassag}x{magas.melyseg}, súlya: {magas.suly} kg.")