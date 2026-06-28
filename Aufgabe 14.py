# Schreiben Sie ein Programm bei dem der User gegen den Computer ein 'Schere-Stein-Papier' Spiel spielt. Das Programm soll 
# 1. vom User einen Input ["Schere", "Stein", "Papier"] bekommen, 
# 2. es soll prüfen ob der Input verarbeitet werden kann, 
# 3. wenn ja, dann soll der Computer zufällig eine eine eigene Entscheidung treffen, welche anschließend gegen den Userinput geprüft wird. 
# 4. Wenn der Input nicht verarbeitet werden kann, soll nur der Nutzer gewarnt werden.

import random                                                                               # Import der Bibliothek Random

def schere_stein_papier():                                                                  # definion der Funktion schere_stein_papier    
    optionen = ["Schere", "Stein", "Papier"]                                                # Liste mit den Optionen erstellen
    user_wahl = input("Wähle Schere, Stein oder Papier: ").capitalize()                     # User Input und Formatiereung (capitalize)
    
    if user_wahl not in optionen:                                                           # Vergleich für ungültige Eingaben
        print("Ungültige Eingabe!")
        return

    computer_wahl = random.choice(optionen)                                                 # Auswahl des Computers
    print(f"Der Computer hat {computer_wahl} gewählt.")                                     # Ausgabe was Computer gewählt hat

    if user_wahl == computer_wahl:                                                          # Vergleich User/Computerwahl
        print("Unentschieden!")
    elif user_wahl == "Schere":
        if computer_wahl == "Papier":
            print("Du gewinnst!")
        else:
            print("Computer gewinnt!")
    elif user_wahl == "Stein":
        if computer_wahl == "Schere":
            print("Du gewinnst!")
        else:
            print("Computer gewinnt!")
    elif user_wahl == "Papier":
        if computer_wahl == "Stein":
            print("Du gewinnst!")
        else:
            print("Computer gewinnt!")

schere_stein_papier()                                                                        # Programm starten