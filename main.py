def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        return "Napaka: deljenje z 0 ni dovoljeno!"
    return a / b

zgodovina = []

while True:
    print("\nPozdrav! Mini kalkulator")
    print("0 = izhod")
    print("1 = seštevanje")
    print("2 = odštevanje")
    print("3 = množenje")
    print("4 = deljenje")

    izbira = input("Kaj želiš narediti? (0, 1, 2, 3 ali 4): ")

    if izbira == "0":
        print("Program se zapira. Nasvidenje!")
        break

    elif izbira in ["1", "2", "3", "4"]:
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))

        if izbira == "1":
            rezultat = sestej(x, y)
            zapis = f"Seštevanje: {x} + {y} = {rezultat}"
        elif izbira == "2":
            rezultat = odstej(x, y)
            zapis = f"Odštevanje: {x} - {y} = {rezultat}"
        elif izbira == "3":
            rezultat = pomnozi(x, y)
            zapis = f"Množenje: {x} * {y} = {rezultat}"
        elif izbira == "4":
            rezultat = deli(x, y)
            zapis = f"Deljenje: {x} / {y} = {rezultat}"

        print(zapis)

        zgodovina.append(zapis)

        if len(zgodovina) > 3:
            zgodovina.pop(0)

        print("\nZadnji 3 izračuni:")
        for element in zgodovina:
            print(element)

    else:
        print("Neveljavna izbira!")