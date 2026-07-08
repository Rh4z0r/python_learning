# Die Filmliste aus `Aufgabe 16` hat einige sehr lange Titel in sich. Schreiben Sie ein Programm das Ihnen den längsten Titel in
# der Liste zurückgibt. Die Funtion sollte dabei nicht nur den Namen des längesten Filmnamens, sondern auch dessen Position in der 
# Liste und dessen Zeichenlänge zurückgeben. 

# Liste mit George Clooney Filmen: [                                                                                                                                   
#    "Title", "Grizzly II: Revenge", "Return to Horror High", 
#    "Return of the Killer Tomatoes", "Red Surf, Unbecoming Age", 
#    "The Harvest", "From Dusk till Dawn", "One Fine Day, Batman & Robin", 
#    "The Peacemaker", "The Thin Red Line", "Out of Sight", "Waiting for Woody", 
#    "Three Kings", "The Book That Wrote Itself", "South Park: Bigger, Longer & Uncut", 
#    "The Perfect Storm"," O Brother", "Where Art Thou?", "Ocean's Eleven", "Spy Kids", 
#    "Confessions of a Dangerous Mind", "Solaris", "Welcome to Collinwood", "Spy Kids 3-D: Game Over", 
#    "Intolerable Cruelty", "Ocean's Twelve", "Good Night", "and Good Luck", "Syriana", "The Good German", 
#    "Michael Clayton", "Ocean's Thirteen", "Sand and Sorrow", "Darfur Now", "Leatherheads", "Burn After Reading", 
#    "Fantastic Mr. Fox", "The Men Who Stare at Goats", "Up in the Air", "The American", "The Ides of March", 
#    "The Descendants", "Gravity", "The Monuments Men", "Annie", "Tomorrowland", "Hail, Caesar!", "Money Monster", 
#    "The Midnight Sky", "Ticket to Paradise"]

liste = [                                                                                                                                   # Definieren der Liste
    "Title", "Grizzly II: Revenge", "Return to Horror High", 
    "Return of the Killer Tomatoes", "Red Surf, Unbecoming Age", 
    "The Harvest", "From Dusk till Dawn", "One Fine Day, Batman & Robin", 
    "The Peacemaker", "The Thin Red Line", "Out of Sight", "Waiting for Woody", 
    "Three Kings", "The Book That Wrote Itself", "South Park: Bigger, Longer & Uncut", 
    "The Perfect Storm"," O Brother", "Where Art Thou?", "Ocean's Eleven", "Spy Kids", 
    "Confessions of a Dangerous Mind", "Solaris", "Welcome to Collinwood", "Spy Kids 3-D: Game Over", 
    "Intolerable Cruelty", "Ocean's Twelve", "Good Night", "and Good Luck", "Syriana", "The Good German", 
    "Michael Clayton", "Ocean's Thirteen", "Sand and Sorrow", "Darfur Now", "Leatherheads", "Burn After Reading", 
    "Fantastic Mr. Fox", "The Men Who Stare at Goats", "Up in the Air", "The American", "The Ides of March", 
    "The Descendants", "Gravity", "The Monuments Men", "Annie", "Tomorrowland", "Hail, Caesar!", "Money Monster", 
    "The Midnight Sky", "Ticket to Paradise"]

def finde_laengsten_namen(liste):                                   # Definieren der Funktion finde_laengsten_namen
    laengster_name = ""                                             # Variable laengster_name definieren
    position = -1                                                   # Definition des Platzhalter-Wertes 
    
    for i, name in enumerate(liste):                                # Indexieren und Namenssuche
        if len(name) > len(laengster_name):                         # Kondition für längster Name
            laengster_name = name                                   # Variablenbestimmung
            position = i                                            # Neue Position setzen 
            
    return laengster_name, position                                 # Rücksprung ins Hauptprogramm

name, pos = finde_laengsten_namen(liste)                            # Name und Position aus der Liste definieren

print(f"Der längste Name ist: '{name}'")                            # Ausgabe des Namens
print(f"Er befindet sich an Position: {pos}")                       # Ausgabe der Position