# Schreiben Sie ein Programm bei dem der User gegen den Computer ein 'Schere-Stein-Papier' Spiel spielt. Das Programm soll 
# 1. vom User einen Input ["Schere", "Stein", "Papier"] bekommen, 
# 2. es soll prüfen ob der Input verarbeitet werden kann, 
# 3. wenn ja, dann soll der Computer zufällig eine eine eigene Entscheidung treffen, welche anschließend gegen den Userinput geprüft wird. 
# 4. Wenn der Input nicht verarbeitet werden kann, soll nur der Nutzer gewarnt werden.

import random                                                                              # Bibliothek Random importieren

def schere_stein_papier():                                                                 # definieren der Funktion schere_stein_papier
    optionen = ["Schere", "Stein", "Papier"]                                               # Liste mit Werten definieren
    
    user_wahl = input("Wähle Schere, Stein oder Papier: ").capitalize()                    # Nutzereingabe erfragen

    if user_wahl not in optionen:                                                          # Validitätsprüfung der Eingabe
        print("Ungültige Eingabe! Bitte wähle genau: Schere, Stein oder Papier.")          # Ausgabe bei ungültigen Eingaben
        return                                                                             # Return

    computer_wahl = random.choice(optionen)                                                # Computer wählt zufällig
    print(f"Der Computer hat {computer_wahl} gewählt.")                                    # Ausgabe was der Computer gewählt hat

    if user_wahl == computer_wahl:                                                         # Vergleich Computer / User
        print("Unentschieden!")                                                            # Ergebnis-Vergleiche
    elif (user_wahl == "Schere" and computer_wahl == "Papier") or \
         (user_wahl == "Stein" and computer_wahl == "Schere") or \
         (user_wahl == "Papier" and computer_wahl == "Stein"):
        print("Du hast gewonnen!")
    else:
        print("Der Computer hat gewonnen!")                                                 # Computer hat gewonnen
schere_stein_papier()                                                                       # PRogramm startenSc