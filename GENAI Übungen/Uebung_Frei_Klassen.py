class Hund:
    # Das ist der Konstruktor (wird beim Erstellen eines neuen Hundes aufgerufen)
    def __init__(self, name, alter):
        self.name = name    # Eigenschaft (Attribut)
        self.alter = alter  # Eigenschaft (Attribut)

    # Das ist eine Methode (eine Aktion, die der Hund ausführen kann)
    def bellen(self):
        print(f"{self.name} sagt: Wuff! 🐾")
        
        
        
namedog = input("Bitte geben Sie den Namen der Töle ein: ")
alterdog = input("Bitte sagen Sie mir wie lange sie schon auf der Welt ist: ")
mein_hund = Hund(namedog , alterdog)

# Wir lassen ihn bellen, damit wir auch etwas im Terminal sehen!
mein_hund.bellen()


class Flaeche:
    def __init__(self, laenge, breite, hoehe):
        self.laenge = laenge
        self.breite = breite
        self.hoehe = hoehe
    
    def flaeche(self):
        m = self.laenge * self.breite * self.hoehe
        return m
    
hoch = int(input("Bitte geben Sie die Höhe ein: "))
lang = int(input("Bitte geben Sie die Länge ein: "))
breit = int(input("Bitte geben Sie die Breite ein: "))

meine_flaeche = Flaeche(hoch, lang, breit)

ergebnis = meine_flaeche.flaeche()
    
print(f"das Volumen beträgt ",ergebnis)

