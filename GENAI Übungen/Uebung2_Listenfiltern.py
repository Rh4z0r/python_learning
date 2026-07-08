# ==========================================
# Aufgabe 2: Listen filtern
# ==========================================
# Schreibe eine Funktion namens 'filter_gerade_zahlen(zahlen_liste)'.
# Diese Funktion bekommt eine Liste von Zahlen übergeben.
# Sie soll eine NEUE Liste zurückgeben (mit 'return' 😉), 
# die NUR die geraden Zahlen aus der ursprünglichen Liste enthält.
#
# Tipp: Du kannst eine leere Liste erstellen (z.B. neue_liste = []) 
# und mit einer for-Schleife durch die 'zahlen_liste' gehen.
# ==========================================

zahlen_liste = [2, 5, 9, 1, 2, 9, 19, 99, 23, 12, 45, 98, 38]
sorted_list = []

def filter_gerade_zahlen(zahlen_liste):
    for z in zahlen_liste:
        if z % 2 == 0:
            sorted_list.append(z)
filter_gerade_zahlen(zahlen_liste)
 
print(f"die geraden Zahlen aus der Liste sind: {sorted_list}")
