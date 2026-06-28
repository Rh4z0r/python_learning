# Aufgabe 3 (Schaltjahre, 2 Punkte)
# Ein Kalenderjahr hat bekanntlich 365 oder 366 Tage. Nach dem Gregorianischen Kalenderjahr
# dauert ein Jahr exakt 365.2425 Tage, also 365 Tage, 5 Stunden, 49 Minuten, 12 Sekunden oder
# anders ausgedruckt: 31.556.952 Sekunden. Man sieht, dass ein Jahr also grob gesprochen einen ¨
# Viertel Tag l¨anger ist als 365 Tage. Um diesen Unterschied zu beheben, hat man Schalttage
# eingefugt. Alle vier Jahre wird mit dem 29. Februar ein Schalttag eingef ¨ ugt. Allerdings machen ¨
# wir damit einen neuen kleinen “Fehler”, denn nun haben wir einen Hundertertstel Tag zuviel. Aus
# diesem Grunde wird alle Hundert Jahre – und zwar, wenn die Jahreszahl durch Hundert teilbar
# ist – auf einen Schalttag verzichtet. So war beispielsweise das Jahr 1900 kein Schaltjahr, obwohl
# es durch vier teilbar war. Man ben¨otigt jedoch noch alle 400 Jahre ein weiteres Korrektiv, dann
# wird ein Schalttag eingefugt, obwohl die Jahreszahl durch Hundert teilbar ist. Nach dieser Regel ¨
# war das Jahr 2000 ein Schaltjahr. Schreiben Sie nun ein Python-Programm, das berechnet, ob eine
# gegebene Jahreszahl ein Schaltjahr ist oder nicht.

hundejahre = int(input("Wie alt ist dein Hund? "))

is_valid_data = hundejahre <= 0 

if hundejahre <=0:
    print("Bitte geben Sie das Alter des Hundes ein. Es muss größer 0 sein.")
elif hundejahre <=1: 
    # Erstes Jahr zählt 14 Menschenjahre
    menschenjahre = hundejahre * 14
elif hundejahre <=2:
    # Das zweite Jahr bringt 8 Jahre dazu (14+8=22)
    menschenjahre = 14 + (hundejahre -1 ) * 8
else: 
    # Ab dem 3. Jahr zählt jedes Jahr 5 Menschenjahre
    menschenjahre = 22 + (hundejahre -2) * 5

if is_valid_data:
    print("Eingabe ist nicht erlaub")

else: 
    print(f"Dein Hund wäre als Mensch etwa {menschenjahre} Jahre alt!")