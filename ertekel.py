def etelertekeles():
    etel_neve = input("Étel neve: ")
    rendelo = input("Étel rendelőjének a neve: ")
    ertekeles = int(input("Értékelés (1-5): "))

    if ertekeles < 0:
        print("Az értékelés nem lehet negatív!")
    elif ertekeles > 5:
        print("5 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")
    print(f"I/A, B: \n \t Étel neve: {etel_neve} \n \t Étel rendelőjének a neve: {rendelo} \n \t Értékelés (1-5): {ertekeles}")
    print("\t Köszönjük az értékelést!")

    