# Opdracht 3.1 - Functie om te berekenen of een getal een priemgetal is
# Maak een functie genaamd "is_priem" die een parameter "getal" accepteert.
# Deze functie moet controleren of het getal een priemgetal is.
# Als het getal een priemgetal is, print dan "Het getal is een priemgetal"
# Als het getal geen priemgetal is, print dan "Het getal is geen priemgetal"
# Als het getal geen integer is, print dan "Het getal is geen integer"

def is_priem(getal):
    if not type(getal == int):
        print("Het getal is geen integer")
        return

    if getal <= 1:
        print("Het getal is geen priemgetal")
        return

    for i in range(2, getal):
        if getal % i == 0:
            print("Het getal is geen priemgetal")
            return

    print("Het getal is een priemgetal")

# Opdracht 3.2 - Functie om een getal naar een binair getal om te zetten
# Maak een functie genaamd "binair" die een parameter "getal" accepteert.
# Deze functie moet het getal omzetten naar een binair getal en printen.
# Als het getal geen integer is, print dan "Het getal is geen integer"
    
def binair(getal):
    if not type(getal == int):
        print("Het getal is geen integer")
        return

    print(bin(getal))

# Opdracht 3.3 - Functie om een getal naar een hexadecimaal getal om te zetten
# Maak een functie genaamd "hexadecimaal" die een parameter "getal" accepteert.
# Deze functie moet het getal omzetten naar een hexadecimaal getal en printen.
# Als het getal geen integer is, print dan "Het getal is geen integer"
    
def hexadecimaal(getal):
    if not type(getal == int):
        print("Het getal is geen integer")
        return

    print(hex(getal))