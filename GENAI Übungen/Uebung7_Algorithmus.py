meine_liste = [14, 58, 2, 99, 31, 7]

def finde_maximum(zahlen_liste):
    groesste_bisher = zahlen_liste[0] 
    

    for z in zahlen_liste:
        if z > groesste_bisher:
            groesste_bisher = z  
        
    return groesste_bisher

# ==========================================
# Test-Bereich 
# ==========================================
ergebnis = finde_maximum(meine_liste)
print("Die größte Zahl ist:", ergebnis)