# ==========================================
# Aufgabe 1: Funktionen & Modulo
# ==========================================
# Schreibe eine Funktion namens 'ist_gerade(zahl)'.
# Diese Funktion soll mithilfe des Modulo-Operators (%) prüfen,
# ob die übergebene 'zahl' gerade ist.
#
# - Wenn sie gerade ist, soll die Funktion True zurückgeben.
# - Wenn sie ungerade ist, soll sie False zurückgeben.
# ==========================================                                              

def ist_gerade(zahl):
    if zahl % 2 == 0: 
        print(f"Die Zahl {zahl} ist gerade.TRUE")
    else:
        print(f"Die Zahl {zahl} ist ungerade.FALSE")
        
try: 
    zahl = int(input("Bitte gib eine Zahl ein, ich prüfe ob sie gerade oder ungerade ist: "))       

    ist_gerade(zahl)

except ValueError:                                                                                  
    print("Bitte geben Sie eine gültige Zahl ein.")  
    
    