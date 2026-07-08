inventar = {
    "Zaubertrank": 3,
    "Apfel": 5,
    "Schwert": 0
}

print("Dein Rucksack:", inventar)
benutztes_item = input("Welches Item möchtest du benutzen? ")


if benutztes_item in inventar and inventar[benutztes_item] > 0: 
    inventar[benutztes_item] -= 1
elif benutztes_item in inventar and inventar[benutztes_item] == 0:
    print("Du hast leider keins mehr davon, do looser... ")
else: 
    print("Das hast du garnicht dabei, du Vollhonk")

# --- DEINE AUFGABE START ---
# Schreibe hier den Code, der Folgendes macht:
# 1. Prüfe zuerst, ob das 'benutztes_item' überhaupt im Dictionary 'inventar' existiert.
# 2. Wenn JA, musst du noch etwas prüfen: Ist die Menge von diesem Item größer als 0?
#    - Wenn noch mindestens eins da ist: Ziehe 1 von der Menge ab (-= 1).
#    - Wenn die Menge schon 0 ist: Gib einfach per print() aus: "Du hast leider keine mehr davon!"
# 3. Wenn NEIN (das Item gibt es gar nicht im Dictionary): Gib per print() aus: "Das hast du gar nicht dabei!"
# --- DEINE AUFGABE ENDE ---

print("Aktuelles Inventar nach der Aktion:", inventar)