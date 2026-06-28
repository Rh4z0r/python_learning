# Aufgabe 1 (Geometrische Formeln, 1 Punkte)
# a) Nehmen wir an, wir haben ein Rechteck mit einer L¨ange von 4 m und einer Breite von 3 m.
# Berechnen Sie die Fl¨ache dieses Rechtecks auf m¨oglichst naive Weise in Python.
# b) Verwenden Sie Variablen mit aussagekr¨aftigen Namen, um Ihre Berechnung verst¨andlicher
# zu machen.
# c) Stellen Sie sich das Rechteck als ein Grundstuck vor, das Sie kaufen m ¨ ¨ochten. Die Stadtverwaltung hat den Preis pro Quadratmeter auf 50¿ festgelegt. Auf diese K¨aufe ist eine Steuer
# von 3,5% zu entrichten. Berechnen Sie den Netto- und Bruttopreis, den Sie zahlen mussten, ¨
# und informieren Sie den Nutzer uber die Zusammensetzung des Bruttopreises. 


#Aufgabe 1
Laenge = 4
Breite = 3
Flaeche = Laenge * Breite
print(Flaeche, "m²")

Preis = 50
Steuer = 0.035 
Nettopreis = Preis * Flaeche
Bruttopreis = Nettopreis * (1 + Steuer)
print ("Bruttopreis: ", Bruttopreis, "     Nettopreis: ", Nettopreis)