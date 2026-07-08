# Unsere Eltern-Klasse (die hast du ja schon perfekt geschrieben!)
class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        
    def hupen(self):
        print("Mööp")

# ==========================================
# Aufgabe 5: Vererbung
# ==========================================
# Die neue Klasse erbt von Auto, indem wir 'Auto' in die Klammern schreiben.
class Feuerwehrauto(Auto):
    def __init__(self, marke, farbe, jahr):# Da wir die __init__ von Auto übernehmen wollen, müssen wir sie hier 
        super().__init__(marke, farbe)
        self.jahr = jahr
    
    def blaulicht_an(self):
        print("Tatü, Tata, Blaulicht ist an")


mein_feuerwehrauto = Feuerwehrauto("Mercedes", "Rot", "2021")
    
print(f"Einsatz für den {mein_feuerwehrauto.farbe}en {mein_feuerwehrauto.marke} mit dem Baujahr {mein_feuerwehrauto.jahr}")
    
mein_feuerwehrauto.hupen()
mein_feuerwehrauto.blaulicht_an()