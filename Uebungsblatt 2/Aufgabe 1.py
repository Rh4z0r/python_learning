# Schreiben Sie ein Program, das auf der Kommandozeile aus einem von Ihnen wählbaren Zeichen
# ein Dreieck mit einer vom User eingegebenen Höhe ausgibt.
# Beispiel: Für die Benutzereingabe 3 und das gewählte Zeichen “#” soll das Programm eine wie
# folgt aussehende Ausgabe erzeugen:

#
##
###
##
#

count = int(input("Bitte geben sie die Höhe des Dreiecks ein: "))           # Abfrage der Höhe des Dreiecks      

for i in range(1, count + 1):                                               # Zeichenberechenung aufsteigend bis Zahl + 1
    print("#" * i)                                                          # Ausgabe (oberer Teil bis Zahl)

for i in range(count -1, 0 ,-1):                                            # Zeichenberechnung absteigend von Zahl -1 bis 0
    print("#" * i)                                                          # Ausgabe (unterer Teil)