import random

lista = {}

def lägg_till_glosa():
    # Lägger till översättning i övningen
    ordet = input("Skriv ordet: ")
    översättning = input("Skriv översättning: ")
    lista[ordet] = översättning
    print(f"{ordet} har lagts till i glos övning.")

def testa_lista():

    if not lista:
        print("Glosor är tom. Lägg till ord först.")
        return

    while True:
        slumpmässigt_ord = random.choice(list(lista.keys()))
        korrekt_översättning = lista[slumpmässigt_ord]
        
        print(f"Översätt ordet: {slumpmässigt_ord}")
        gissning = input("Din gissning: ").lower()

        if gissning.lower() == korrekt_översättning.lower():
            print("Rätt svar!")
        else:
            print(f"Fel svar. Rätt översättning är: {korrekt_översättning}")

        fortsätt_testa = input("Vill du testa ett annat ord? (ja/nej): ")
        if fortsätt_testa.lower() != "ja":
            break

while True:
    print("\nVälj en åtgärd:")
    print("1. Lägg till ett ord")
    print("2. Öva glosor")
    print("3. Avsluta")

    val = input("Ditt val: ")

    if val == "1":
        lägg_till_glosa()
    elif val == "2":
        testa_lista()
    elif val == "3":
        break
    else:
        print("Välj en av alternativen ovan, Försök igen.")

print("Tack för att du använde Alloush och Filippas glosprogram!")