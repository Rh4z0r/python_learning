# Schreiben Sie eine Funktion

# fak(number)


# die die Fakultät einer gegebenen Zahl berechnet und zurückgibt. 

def fakt(number):                                                                                                    # Definition der Funktion fak(number)
    ergebnis = 1                                                                                                    # Ergebnisdefinition (kleinster Wert ist 1x1=1)
    for i in range(1, number + 1):                                                                                  # for-Schleife überprüft die Bandbreite von Zahl 1 bis Eingabe +1 
        ergebnis *= i                                                                                               # Berechnung des Ergebnisses mit der Variablen i
    return ergebnis                                                                                                 # Rückgabe des Ergebnissen

entry = 3        # Nutzereingabe der Zahl erfragen

print(f"Die Fakultät von {entry} ist: {fakt(entry)}")                                                                # Ausgabe des Ergebnisses