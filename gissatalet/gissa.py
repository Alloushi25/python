# Denna uppgift ska vi öva variabler, villkor och loopar
import random
import os
os.system("cls" if os.name == "nt" else "clear")

print("\n---------------------------------------------")
print(".:GissaTalet:.")

print("Gissa ett tal mellan 1 - 10 och pröva om du är ass eller bra, du får 3st försök!\n")

slumptal = random.randint(1, 10)
# print(slumptal)

i = 0
hitta = False

# loopar
max_forsok = 3  # Maximalt antal försök

while i < max_forsok:

    gissatal = int(input("Mata in tal: "))

    if slumptal == gissatal:
        hitta = True
        print("\n Rätt svar! Grattis du är inte en idiot \n")
        break
    elif slumptal < gissatal:
        i += 1
        forsok_kvar = max_forsok - i
        print(f"Det var fel retard! Talet är lägre. Du har {forsok_kvar} försök kvar.")
    else:
        i += 1
        forsok_kvar = max_forsok - i
        print(f"Det var fel retard! Talet är högre. Du har {forsok_kvar} försök kvar.")

if hitta:
    print("\n Bra jobbat, här får du en bugatti")

else:
    print(f"Du har slut på försök. Det hemliga talet var {slumptal}. Bättre lycka nästa gång!")

print("\n--------------------------------------------------------------")