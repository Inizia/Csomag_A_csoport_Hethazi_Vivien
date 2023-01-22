class Pogyasz:
    def __init__(self, ertek):
        self.szelesseg = int(ertek[0])
        self.magassag = int(ertek[1])
        self.melyseg = int(ertek[2])
        self.suly = int(ertek[3])


    def __str__(self):
        return f"{self.szelesseg}; {self.magassag}; {self.melyseg}; {self.suly}"