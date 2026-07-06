# ==========================================
# Aufgabe 3: Dictionaries 
# ==========================================
# Schreibe eine Funktion namens 'inventar_update(inventar, item)'.
# 'inventar' ist ein Dictionary, 'item' ist ein String (z.B. "Apfel").
# 
# Die Funktion soll Folgendes prüfen:
# 1. Gibt es das 'item' schon als Key im Dictionary 'inventar'?
#    -> Wenn ja: Erhöhe den dazugehörigen Value (die Anzahl) um 1.
# 2. Wenn nein:
#    -> Lege den Key neu an und setze den Value auf 1.
# 
# Gib am Ende das aktualisierte Dictionary mit 'return' zurück.
# ==========================================
inventar = { "Apfel": 1, "Birne": 2, "Banane": 3, "Kirsche": 4, "Melone": 1, "Traube": 15}

# 1. Funktion GANZ OBEN definieren (nur einmal)
def inventar_update(inventar, item):
    if item in inventar:
        inventar[item] += 1
    else:    
        inventar[item] = 1

# 2. Schleife starten
while True:
    eingabe = input("Bitte geben Sie ein Obst ein (oder 'ende' zum Abbrechen): ")

    # 3. ZUERST prüfen, ob wir abbrechen wollen!
    if eingabe.lower() == "ende":
        print("Eingabe ist beendet.")
        break  # WICHTIG: Das break ist jetzt eingerückt!

    # 4. Wenn NICHT abgebrochen wurde, updaten wir das Inventar
    inventar_update(inventar, eingabe)
    print("Aktueller Stand:", inventar)

# Das print ganz am Schluss, wenn die Schleife beendet ist
print("Dein fertiges Inventar:", inventar)