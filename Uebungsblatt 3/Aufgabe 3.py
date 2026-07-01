# F¨ uhren Sie die folgenden beiden Umwandlungen zwischen Schleifentypen durch.
# a) Wandeln Sie die folgenden list comprehension in eine normale for-Schleife um.
# customers = [
# ["Max"
# ,
# ["Martina"
# ["Gabi"
# ,
# "Mustermann"
# ,
# "01.01.83"],
# "Musterfrau"
# ,
# "Meier"
# ,
# "02.02.84"],
# ,
# "03.03.85"]
# ]
# last_names = [person[1] for person in customers]
# b) Wandeln Sie die folgende for-Schleife in eine while-Schleife um.
# numbers = [1, 4, 2, 8, 5]
# squared_numbers = []
# for number in numbers:
# squared_numbers.append(number * number)
# 1
# c) Wandeln Sie die folgenden while-Schleife in eine for-Schleife um.
# import random
# secret_number = random.randint(1, 100) # Generate random number
# guess = 0
# while guess != secret_number:
# guess = int(input("Guess a number between 1 and 100: "))
# if guess > secret_number:
# print("Too high! Guess again.
# ")
# elif guess < secret_number:
# print("Too low! Guess again.
# ")
# else:
# print("You guessed it! The number was", secret_number)