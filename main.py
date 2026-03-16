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

print("Pozdrav! Mini kalkulator")
print("0 = izhod")
print("1 = seštevanje")
print("2 = odštevanje")
print("3 = množenje")
print("4 = deljenje")

izbira = input("Kaj želiš narediti? (0, 1, 2, 3 ali 4): ")

if izbira == "0":
    print("Program se zapira. Nasvidenje!")
elif izbira == "1":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = sestej(x, y)
    print(f"Rezultat seštevanja števil {x} in {y} je {rezultat}.")
elif izbira == "2":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = odstej(x, y)
    print(f"Rezultat odštevanja števil {x} in {y} je {rezultat}.")
elif izbira == "3":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = pomnozi(x, y)
    print(f"Rezultat množenja števil {x} in {y} je {rezultat}.")
elif izbira == "4":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = deli(x, y)
    print(f"Rezultat deljenja števil {x} in {y} je {rezultat}.")
else:
    print("Neveljavna izbira!")