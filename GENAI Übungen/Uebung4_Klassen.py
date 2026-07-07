# ==========================================
# Aufgabe 4: Klassen schreiben
# ==========================================
# Schreibe eine Klasse namens 'Auto'.
# 
# 1. Sie soll eine __init__-Methode haben, die die Eigenschaften 
#    'marke' und 'farbe' für das Auto setzt.
# 2. Schreibe außerdem eine Funktion (Methode) in der Klasse 
#    namens 'hupen', die einfach "Mööp!" auf dem Bildschirm ausgibt.
# ==========================================

class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        
    def hupen(self):
        print("Mööp")
    
mein_auto = Auto("VW", "Rot")
    
print(f"Mein Auto ist ein {mein_auto.farbe}er {mein_auto.marke}.")
    
mein_auto.hupen()