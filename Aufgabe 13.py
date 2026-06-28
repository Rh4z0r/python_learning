# Die Nullstellen x1, x2 einer quadratischen Gleichung berechnet man mit folgender Formel:
# $$x_{1,2} = {-b\pm\sqrt{b^2 - 4ac} \over 2a}$$
# Schreiben Sie ein Programm, dass vom Nutzer die drei Parameter a,b,c erfrägt und mit der Formel x1 und x2 berechnet. Diese sollen anschließend ausgegeben werden. 

import math                                                                                                     # Importiere Bibliothek Math

print("Berechnung der Nullstellen für: ax^2 + bx + c = 0")                                                      # Aufgabenstellung printen

a = float(input("Gib a ein: "))                                                                                 # Inputaufforderung a
b = float(input("Gib b ein: "))                                                                                 # Inputaufforderung b
c = float(input("Gib c ein: "))                                                                                 # Inputaufforderung c

diskriminante = b**2 - 4*a*c                                                                                    # berechnen der Diskriminanten

if diskriminante < 0:                                                                                           # Wenn Diskriminante < 0 gibt es keine reellen Nullstellen
    print("Die Gleichung hat keine reellen Nullstellen.")                                                       # Ausgabe
else:                    
    x1 = (-b + math.sqrt(diskriminante)) / (2*a)                                                                # Formel mit + berechnen
    x2 = (-b - math.sqrt(diskriminante)) / (2*a)                                                                # Formel mit - berechnen
    
    print(f"Die Nullstellen sind x1 = {x1} und x2 = {x2}")                                                      # Ausgabe des Ergebnisses
