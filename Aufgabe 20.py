# Schreiben Sie ein Programm zur Berechnung der Reihensumme von $$1 / 2+2/3+3/4+...+n/n+1$$ mit einer gegebenen Eingabe `n` über `input()`. Es gilt `(n>0)`.

# Beispiel: Wenn das folgende n als Eingabe in das Programm gegeben wird: `5`, dann sollte die Ausgabe des Programms sein: `3.55`

# Hinweise: Verwenden Sie `float()`, um eine Ganzzahl in eine Fließkommazahl umzuwandeln.

n = int(input("Bitte gib eine positive Zahl n ein: "))                                  # Eingabe des Benutzers entgegennehmen und in einen Integer umwandeln

if n > 0:                                                                               # Prüfen, ob n > 0 ist
    summe = 0.0
    

    for i in range(1, n + 1):                                                           # Die Schleife läuft von 1 bis n. /.  range(1, n + 1) erzeugt Zahlen von 1 bis n
        # Den aktuellen Bruch berechnen: i / (i + 1)
        bruch = i / (i + 1)                                                             # Den aktuellen Bruch berechnen: i / (i + 1)
        summe += bruch                                                                  
    
    print(round(summe, 2))                                                              # Ergebnis auf 2 Nachkommastellen gerundet ausgeben
else:
    print("Bitte gib eine Zahl größer als 0 ein.")                                      # Ausgabe 