rezultat = []
while True:
    while True:
        simbol_ales = input("Avem urmatoarele optiuni:\n"
                            "1) \'Adunare\'(+) \n"
                            "2) \'Inmultire\'(*)\n"
                            "3) \'Impartire\'(/) \n"
                            "4) \'Diferenta\'(-) \n"
                            "Va rog introduceti optiunea (semnul operatiei): ")
        if simbol_ales == '+' or simbol_ales == '*' or simbol_ales == '/' or simbol_ales == '-':
            break
        else:
            print("\nVa rugam sa alegti un semn valid\n")

    while True:
        numar1 = input("Va rog introduceti primul numar: ")
        if numar1.isnumeric():
            numar1 = int(numar1)
            break
        else:
            print("Va rog sa introduceti un numar valid")

    while True:
        numar2 = input("Va rog introduceti al 2-lea numar: ")
        if numar2.isnumeric():
            numar2 = int(numar2)
            break
        else:
            print("Va rog sa introduceti un numar valid")

    if numar2 == 0 and simbol_ales == "/":
        print("\nNu puteti imparti la 0 va rugam sa refaceti operatia\n")
        continue

    if simbol_ales == "+":
        rezultat.append(numar1 + numar2)
    elif simbol_ales == "*":
        rezultat.append(numar1 * numar2)
    elif simbol_ales == "/":
        rezultat.append(numar1 / numar2)
    else:
        rezultat.append(numar1 - numar2)

    continuare = input("Do you want to continue (YES/no): ")
    if continuare.lower() == "no":
        print(rezultat)
        break
