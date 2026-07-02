# Führen Sie die folgenden beiden Umwandlungen zwischen Schleifentypen durch.
# a) Wandeln Sie die folgenden list comprehension in eine normale for-Schleife um.

customers = [
["Max", "Mustermann", "01.01.83"],
["Martina", "Musterfrau", "02.02.84"],
["Gabi", "Meier", "03.03.85"]
]
last_names = [person[1] for person in customers]

# for-Schleife

customers = [                                                           # Definieren der Listen
["Max", "Mustermann", "01.01.83"],                          
["Martina", "Musterfrau", "02.02.84"],
["Gabi", "Meier", "03.03.85"]
]

for person in customers:                                                # For Bedingung
    last_names.append(person[1])                                        # Familienname in die Liste last_names schreiben

print(last_names)                                                       # Ausgeben der Liste last_names

# b) Wandeln Sie die folgende for-Schleife in eine while-Schleife um.

numbers = [1, 4, 2, 8, 5]
squared_numbers = []
for number in numbers:
    squared_numbers.append(number * number)

# while-Schleife

number = [1, 4, 2, 8, 5]
squared_numbers = []

index = 0
while index < len(numbers):
    number = numbers[index]
    squared_numbers.append(number * number)
    index += 1

print(squared_numbers)


# c) Wandeln Sie die folgenden while-Schleife in eine for-Schleife um.

import random
secret_number = random.randint(1, 100) # Generate random number
guess = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > secret_number:
        print("Too high! Guess again.")
    elif guess < secret_number:
        print("Too low! Guess again.")
    else:
        print("You guessed it! The number was", secret_number)

# for-Schleife

import random
secret_number = random.randint(1, 100)                  # Zufällige Nummer generieren
max_versuche = 5

print("Du hast 5 Versuche, um die Zahl zu erraten!")

for versuch in range(max_versuche):
    guess = int(input(f"Versuch {versuch + 1}: "))
    if guess > secret_number:
        print("Zu hoch!")
    elif guess < secret_number:
        print("Zu niedrig!")
    else:
        print("Gewonnen!")
        break
else:
    print(f"Verloren! Die Zahl war {secret_number}.")
                                                                                              


