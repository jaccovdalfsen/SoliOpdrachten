# Opdracht 2.1 Functie met if statement
# Maak een functie genaamd "check" die een parameter "getal" accepteert.
# Als het getal groter is dan 10, print dan "Het getal is groter dan 10"
# Als het getal kleiner is dan 10, print dan "Het getal is kleiner dan 10"
# Als het getal gelijk is aan 10, print dan "Het getal is gelijk aan 10"
# Als het getal geen integer is, print dan "Het getal is geen integer"

def check(getal):
    if getal > 10:
        print("Het getal is groter dan 10")
    elif getal < 10:
        print("Het getal is kleiner dan 10")
    elif getal == 10:
        print("Het getal is gelijk aan 10")
    else:
        print("Het getal is geen integer")

# Opdracht 2.2 Functie met voor even en oneven getallen
# Maak een functie genaamd "switch" die een parameter "getal" accepteert.
# Als het getal even is, print dan "Het getal is even"
# Als het getal oneven is, print dan "Het getal is oneven"
# Als het getal geen integer is, print dan "Het getal is geen integer"
        
def switch(getal):
    if type(getal) == int:
        if getal % 2 == 0:
            print("Het getal is even")
        else:
            print("Het getal is oneven")
    else:
        print("Het getal is geen integer")

# Opdracht 2.3 Functie met for loop
# Maak een functie genaamd "forloop" die een parameter "getal" accepteert.
# Deze functie moet een for loop hebben die van 0 tot het getal loopt en elk getal print.
# Als het getal geen integer is, print dan "Het getal is geen integer"

def forloop(getal):
    if type(getal) == int:
        for i in range(getal):
            print(i)
    else:
        print("Het getal is geen integer")

#Opdracht 2.4 Functie met while loop
# Maak een functie genaamd "whileloop" die een parameter "getal" accepteert.
# Deze functie moet een while loop hebben die van 0 tot het getal loopt en elk getal print.
# Als het getal geen integer is, print dan "Het getal is geen integer"
        
def whileloop(getal):
    if type(getal) == int:
        i = 0
        while i < getal:
            print(i)
            i += 1
    else:
        print("Het getal is geen integer")

def main():
    getal = int(input("Voer een getal in: "))
    check(getal)
    switch(getal)
    forloop(getal)
    whileloop(getal)

main()