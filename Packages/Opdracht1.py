# Opdracht 1.1 - Hello World
# Print "Hello World!" op de console
print("Hello World!")

# Opdracht 1.2 - Functie zonder parameter
def goedenavond():
    print("Goedenavond")

# Opdracht 1.3 - Functie met parameter
# Zorg ervoor dat de naam op de console wordt geprint.
def groet(naam):
    print(f"Hallo, {naam}!")

# Opdracht 1.4 - Functie om een keersom te maken
def keer(a: int, b: int):
    antwoord = a * b
    print(f"Het antwoord op deze keersom is: {antwoord}")

# Main functie 
def main():
    goedenavond()

    naam = input("Voer je naam in: ")
    groet(naam)

    cijfer1 = int(input("Voer het eerste cijfer voor de keersom in: "))
    cijfer2 = int(input("Voer het tweede cijfer in: "))
    keer(cijfer1, cijfer2)

# Dit zorgt ervoor dat de main functie wordt aangeroepen.
# Hier hoef je niet aan te zitten
main()