# Betrachten Sie das Beispiel auf Folie 26 von Foliensatz 4 “Data Structures”. Hier wird demon-
# striert, dass das Suchen von 1000 zuf¨ alligen Zahlen in einer Liste von 100 000 Zahlen um mehrere
# Gr¨ oßenordnungen langsamer ist als in einem gleich großen Set. Erkl¨ art werden kann dies mit der
# sogenannten Laufzeitkomplexit¨ at der darunterliegenden Suchalgorithmen. W¨ ahrend in einer Liste
# bei Verdopplung der Gr¨ oße auch der Suchaufwand ca. doppelt so groß wird, steigt der Suchauf-
# wand in Sets nur in ca. log2-facher Beziehung an. In dieser Aufgabe sollen Sie den dazugeh¨ origen
# Code selbst schreiben und Experimente damit durchf¨ uhren. Gehen Sie dazu wie folgt vor:
# Recherchieren Sie, wie Sie mit Hilfe des random Moduls eine Liste und ein Set mit einer be-
# stimmten Anzahl von Zufallszahlen ohne zur¨ ucklegen aus einem festgelegten Intervall ziehen
# k¨
# onnen.
# Recherchieren Sie, wie Sie mit Hilfe des time Moduls die Ausf¨ uhrungszeit einiger Code-Zeilen
# messen k¨
# onnen.
# Erstellen Sie sich Listen/Sets mit jeweils 10 000, 100 000, 500 000 und 1 000 000 Zufallszahlen,
# die ohne zur¨ ucklegen aus dem Intervall [0, 10000000] gezogen wurden
# Pr¨ ufen Sie mit Hilfe des in Befehls 1000 mal, ob eine zuf¨ allig gezogene Zahl aus dem Intervall
# [0, 10000000] in der Liste/dem Set enthalten ist. Messen Sie dabei jeweils die ben¨ otigte Zeit.
# Vergleichen Sie die Ergebnisse der unterschiedlich großen Listen und Sets miteinander. Wie ¨ außern
# sich die Auswirkungen der beiden Datenstrukturen?