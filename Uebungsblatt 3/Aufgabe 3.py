# Führen Sie die folgenden beiden Umwandlungen zwischen Schleifentypen durch.
# a) Wandeln Sie die folgenden list comprehension in eine normale for-Schleife um.

# Definiere die Kundenliste als Liste von Einträgen [Vorname, Nachname, Geburtsdatum]
customers = [
    ["Max", "Mustermann", "01.01.83"],
    ["Martina", "Musterfrau", "02.02.84"],
    ["Gabi", "Meier", "03.03.85"]
]
# Erstelle eine Liste mit allen Nachnamen mittels List Comprehension
last_names = [person[1] for person in customers]

# for-Schleife: die gleiche Transformation ohne List Comprehension
customers = [
    ["Max", "Mustermann", "01.01.83"],
    ["Martina", "Musterfrau", "02.02.84"],
    ["Gabi", "Meier", "03.03.85"]
]
last_names = []                                                                                          # Leere Liste zum Befüllen mit Nachnamen

for person in customers:                                                                                 # Durchlaufe jede Person in der Kundenliste
    last_names.append(person[1])                                                                         # Füge den Familiennamen zur Liste hinzu

print(last_names)                                                                                        # Ausgabe der Liste der Nachnamen

# b) Wandeln Sie die folgende for-Schleife in eine while-Schleife um.

numbers = [1, 4, 2, 8, 5]                                                                                # Liste der Zahlen
squared_numbers = []                                                                                     # Leere Liste für die Quadrate

for number in numbers:                                                                                   # Normale for-Schleife
    squared_numbers.append(number * number)                                                              # Quadrat berechnen und hinzufügen

# while-Schleife: die gleiche Transformation mit Indexverwaltung
numbers = [1, 4, 2, 8, 5]                                                                                # Liste der Zahlen erneut definieren
squared_numbers = []                                                                                     # Leere Liste für die Quadrate
index = 0                                                                                                # Startindex für die while-Schleife

while index < len(numbers):                                                                              # Schleife solange der Index im Bereich ist
    number = numbers[index]                                                                              # Aktuelle Zahl aus der Liste lesen
    squared_numbers.append(number * number)                                                              # Quadrat berechnen und hinzufügen
    index += 1                                                                                           # Index erhöhen, um zur nächsten Zahl zu wechseln

print(squared_numbers)                                                                                   # Ausgabe der quadratischen Zahlen

# c) Wandeln Sie die folgende while-Schleife in eine for-Schleife um.

import random                                                                                            # Modul für Zufallszahlen importieren
secret_number = random.randint(1, 100)                                                                   # Zufällige Zahl zwischen 1 und 100 generieren

# while-Version: Zahl erraten lassen, bis sie stimmt
guess = 0                                                                                                # Startwert für die Benutzereingabe
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))                                             # Benutzereingabe lesen
    if guess > secret_number:
        print("Too high! Guess again.")                                                                  # Hinweis, wenn die Zahl zu groß ist
    elif guess < secret_number:
        print("Too low! Guess again.")                                                                   # Hinweis, wenn die Zahl zu klein ist
    else:
        print("You guessed it! The number was", secret_number)                                           # Erfolgsmeldung

# for-Schleife: bis zu 5 Versuche erlauben
secret_number = random.randint(1, 100)                                                                   # Neue Zufallszahl generieren
max_versuche = 5                                                                                         # Maximale Anzahl der Versuche festlegen

print("Du hast 5 Versuche, um die Zahl zu erraten!")

for versuch in range(max_versuche):                                                                      # Schleife über die Versuchszahl
    guess = int(input(f"Versuch {versuch + 1}: "))                                                       # Benutzereingabe lesen
    if guess > secret_number:
        print("Zu hoch!")                                                                                # Hinweis, wenn zu hoch geraten wurde
    elif guess < secret_number:
        print("Zu niedrig!")                                                                             # Hinweis, wenn zu niedrig geraten wurde
    else:
        print("Gewonnen!")                                                                               # Erfolgsmeldung
        break                                                                                            # Schleife vorzeitig beenden bei korrektem Tipp
else:
    print(f"Verloren! Die Zahl war {secret_number}.")                                                    # Nachricht bei fehlgeschlagenen Versuchen


