# ==========================================
# Aufgabe 8: List Comprehension
# ==========================================
# Hier ist eine "alte" for-Schleife, die alle Zahlen 
# aus der Liste verdoppelt und in eine neue Liste packt.

alte_liste = [1, 2, 3, 4, 5]

verdoppelt_alt = []
for zahl in alte_liste:
    verdoppelt_alt.append(zahl * 2)


verdoppelt_neu = [zahl * 2 for zahl in alte_liste]

# ==========================================
# Test-Bereich 
# ==========================================
print("Das alte Ergebnis:", verdoppelt_alt)
print("Dein neues Ergebnis:", verdoppelt_neu)
# Beide Ausgaben sollten exakt [2, 4, 6, 8, 10] sein!