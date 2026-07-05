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

eingabe = input("Bitte geben sie ein Obst ein: ")

def inventar_update(inventar, item):
    if item in inventar:
        inventar[item] += 1
    else:    
        inventar[item] = 1
        
inventar_update(inventar, eingabe)

print(inventar)
