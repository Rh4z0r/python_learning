# Aufgabe 2 (Hundejahre, 2 Punkte)
# Kinder und Hundeliebhaber stellen sich h¨aufig die Frage, wie alt ihr Hund wohl w¨are, wenn er
# kein Hund, sondern ein Mensch w¨are. Landl¨aufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert. Je nach Hundegr¨oße und Rasse sieht die
# Umrechnung jedoch etwas komplizierter aus, z.B.:
#  Ein einj¨ahriger Hund entspricht in etwa einem 14-j¨ahrigen Menschen.
#  2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
#  Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.
# Schreiben Sie ein Programm, das das Alter eines Hundes erfragt und dann nach obiger Methode
# berechnet, welchem Alter in Menschenjahren dies entspricht.

hundejahre = float(input("Wie alt ist dein Hund? "))

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

print(f"Dein Hund wäre als Mensch etwa {menschenjahre} Jahre alt!")