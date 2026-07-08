# Erstellen Sie eine Klasse namens `Rectangle`, die mit einer Länge und einer Breite konstruiert werden kann. 
# Die Klasse `Rectangle` hat eine Methode `area()`, mit der die Fläche berechnet werden kann.

import math                                                                                 # Bibliothek math importieren

laenge = int(input("Bitte geben Sie die Länge des Rechtecks in cm ein: "))
breite = int(input("Bitte geben Sie die Breite des Rechtecks in cm ein: "))

class Rectangle:                                                                            # Erstellen der Klasse
    def __init__(self, length, width):                                                      # Konstruktor
        self.length = length                                                                # Länge definieren
        self.width = width                                                                  # Breite definieren

    def area(self):                                                                         # Area Fläche
        return self.length * self.width                                                     # Flächenberechnung

mein_rechteck = Rectangle(laenge, breite)                                                   # Beispielrechteck 
print(f"Die Fläche des Rechtecks beträgt: {mein_rechteck.area()}")                          # Ausgabe der Rechtecksfläche