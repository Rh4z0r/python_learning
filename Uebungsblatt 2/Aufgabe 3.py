# a) Spezifizieren Sie, wie oft ein von Ihnen gewähltes Zeichen maximal wiederholt werden soll.
# Verwenden Sie dann list comprehension, um eine Liste mit aufsteigend vielen Wiederholun-
# gen dieses Zeichens zu erzeugen.
# Beispiel: Mit gewähltem Zeichen “#” und maximal 3 Wiederholungen soll ihre Liste wie
# folgt aussehen: [’#’, ’##’, ’###’]
# b) Multiplizieren Sie eine Zahl nacheinander mit Faktoren, die in einer Liste gespeichert sind.
# Speichern Sie alle Ergebnisse mit Hilfe von list comprehension in einer Liste.
# Beispiel: Zahl 3 und Faktoren [1, 2, 3] soll die Liste [3, 6, 9] ergeben.
# c) Starten Sie mit einer Liste, die Ganzzahlen enthält. Erzeugen Sie daraus mit Hilfe von list
# comprehension zwei Listen. Eine der Listen soll alle geraden Zahlen der Eingabeliste enthal-
# ten, die andere alle ungeraden Zahlen. Geben Sie danach beide Listen auf der Kommandozeile
# aus. einem von Ihnen wählbaren
# Beispiel: Aus der Liste [1, 2, 3] sollen die Listen [2] und [1, 3] erzeugt werden.

zeichen = "#"                                                                           # Deklaration des gewählten Zeichens
max_wiederholungen = 3                                                                  # Deklaration der maximalen Wiederholungen                           
zeichen_liste = [zeichen * i for i in range(1, max_wiederholungen + 1)]                 # List comprehension zur Erzeugung der Liste mit aufsteigend vielen Wiederholungen des gewählten Zeichens
print(zeichen_liste)                                                                    # Ausgabe

zahl = 3                                                                                # Deklaration der Zahl
faktoren = [1, 2, 3]                                                                    # Deklaration der Faktoren
ergebnisse = [zahl * faktor for faktor in faktoren]                                     # List comprehension zur Erzeugung der Liste mit den Ergebnissen der Multiplikation
print(ergebnisse)                                                                       # Ausgabe

zahlen = [1, 2, 3, 4, 5]                                                                # Deklaration der Eingabeliste
gerade_zahlen = [zahl for zahl in zahlen if zahl % 2 == 0]                              # List comprehension zur Erzeugung der Liste mit geraden Zahlen
ungerade_zahlen = [zahl for zahl in zahlen if zahl % 2 != 0]                            # List comprehension zur Erzeugung der Liste mit ungeraden Zahlen
print(gerade_zahlen)                                                                    # Ausgabe gerade Zahlen      
print(ungerade_zahlen)                                                                  # Ausgabe ungerade Zahlen 

