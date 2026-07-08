# Berechnen Sie die Länge von mehreren eingegebenen Wörtern (“Strings”). Schreiben Sie hierfür 
# ein Programm, das zunächst die Anzahl einzugebender Wörter abfrägt, sagen wir k. Dann sollte
# k Mal nach einem Wort (per input()) gefragt werden und jedes Wort zu einer Liste hinzugefügt
# werden. Berechnen Sie dann mit Hilfe einer for-Schleife die Gesamtlänge (in Buchstaben) aller
# eingegebenen Wörter.
# Beispiel: Bei k = 2 und den Eingabewörtern “THI” (3 Buchstaben) und “WI” (2 Buchstaben) soll
# das Ergebnis 5 sein.

liste = []
k = int(input("Bitte geben Sie die Anzahl der Wörter ein: "))                   # Abfrage der Anzahl der Wörter
for i in range(k):                                                              # for Schleife für i in range von k   
    word = input("Bitte geben Sie ein Wort ein: ")                              # Abfrage der Wörter (so oft wie mit k definiert wurde)
    liste.append(word)                                                          # Wort in Liste einfügen

length = 0                                                                      # Grundlänge = 0
for word in liste:                                                              # for Schleife für Wortliste
    length += len(word)                                                         # Längenkondition (Buchstabe = len)

print("Die Gesamtlänge der eingegebenen Wörter beträgt:", length)               # Ausgabe der Gesamtanzahl der Buchstaben
