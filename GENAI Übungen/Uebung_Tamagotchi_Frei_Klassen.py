# 🐾 Das Tamagotchi-Projekt (Virtuelles Haustier)
# Deine Aufgabe ist es, einen Bauplan für ein virtuelles Haustier zu schreiben. Hier geht es nicht nur um eine einfache Rechnung, sondern um Zustände, die sich ständig verändern und kontrolliert werden müssen.
#
# Die Anforderungen:
#
# Die Klasse: Erstelle eine Klasse namens Haustier.
#
# Die Eigenschaften (__init__):
#
# name (wird bei der Erstellung als Parameter übergeben).
#
# hunger (startet standardmäßig bei 50).
#
# energie (startet standardmäßig bei 100).
#  
# Die Methoden (Das Verhalten):
#
# fuettern(futter_wert): Senkt den Hunger um den angegebenen futter_wert.
#
# Der Haken: Der Hunger darf niemals unter 0 fallen! Du musst das im Code abfangen.
# 
# spielen(zeit): Verbraucht Energie (z. B. zeit * 2) und macht das Tier hungriger (z. B. zeit * 1).
#
# Der Haken: Die Energie darf nicht unter 0 fallen. Wenn das Tier nicht genug Energie für die Spielzeit hat, weigert es sich zu spielen (Gib eine entsprechende Print-Meldung aus).
#
# schlafen(): Füllt die Energie komplett auf 100 auf, erhöht den Hunger aber um 10.
#
# status(): Gibt eine schicke Übersicht aus, wie es deinem Tier gerade geht (z. B. "Bello: Energie 80/100, Hunger 40/100").
#
# 🔥 Der extra Biss (Bonus-Challenge):
# Wenn der Hunger über 100 steigt, ist das Spiel vorbei (Game Over) und das Tier haut ab, um sich woanders Futter zu suchen. Baue diese Überprüfung so ein, dass sie nach jeder Aktion checkt, ob das Tier noch da ist. Erstelle am Ende deines Codes ein Objekt und teste alle Funktionen durch!
# 
# Wie klingt das für dich – stürzt du dich direkt mutig in den Code, oder brauchst du vorher noch einen kleinen Tipp, wie du die Grenzen (nicht unter 0, nicht über 100) am besten abfängst? 🧐
#

class Haustier:
    def __init__(self, name):
        self.name = name
        self.hunger = 50    
        self.energie = 100
        self.lebt = True
    
    def check_game_over(self):
        if self.hunger > 100: 
            self.lebt = False
            print(f"💀 Spiel ist zu Ende, da der Hungerwert von {self.name} über 100 angestiegen ist.") 
        
    def fuettern(self,futter_wert):
        self.hunger = self.hunger - futter_wert
        
        if self.hunger < 0: 
            self.hunger = 0
            
        print(f"Mampf! {self.name} wurde gefüttert. Hunger ist jetzt auf {self.hunger}.")
    
    def spielen(self, zeit): 
        if self.energie < (zeit * 2):
            print(f" Meine Energie ({self.energie}) ist zu niedrig zum spielen.")
            
        else:
            self.energie = self.energie - zeit * 2
            self.hunger = self.hunger + 10     
            print(f"Juhu! {self.name} hat gespielt. (Enerige: {self.energie}, Hunger: {self.hunger})")
            self.check_game_over()
        
    def schlafen(self):
        self.energie = 100
        self.hunger = self.hunger + 10
        print(f"Zzz... {self.name} hat geschlafen. Seine Energie ist voll!")
        self.check_game_over()
            
    def status(self):
        print(f"{self.name} hat eine Hungerwert von {self.hunger} und einen Energiewert von {self.energie}")

print("Willkommen bei deinem Tamagotchi.")
tier_name = input("Bitte gib deinem Tamagotchi einen Namen:")
mein_tier = Haustier(tier_name)

while mein_tier.lebt:
    print("\n" + "="*30)
    mein_tier.status()
    
    print("\nWas möchtest du tun?")
    print("[f] Füttern")
    print("[s] Spielen")
    print("[z] Schlafen Zzz")
    print("[b] Spiel beenden")

    aktion = input("Deine Wahl: ")

    if aktion == "f":
        mein_tier.fuettern(20)
    elif aktion == "s":
        mein_tier.spielen(10)
    elif aktion == "z":
        mein_tier.schlafen()
    elif aktion == "b":
        print(f"Tschüss! {mein_tier_name} winkt dir hinterher.")
        break
    else: 
        print("Huch das habe ich nicht verstanden. Bitte drücke f, s, z oder b.")
    
    
        