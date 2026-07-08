waffen_schaden = {
    "Schwert": 15,
    "Bogen": 12,
    "Dolch": 8,
    "Axt": 20
}

print("Willkommen beim Schmied! 🔨")
print(waffen_schaden.keys())                            ##ä###########

waffe = input("Gib die die Waffe, die verbessern möchtest ein: ")

if waffe in waffen_schaden:
    waffen_schaden[waffe] += 1
    print("Deine Waffe beginnt zu blinken.")
else: 
    print("das gibts nicht du idiot")

# --- DEINE AUFGABE START ---

# 1. Zeige dem Spieler zuerst an, welche Waffen überhaupt da sind. 
#    Tipp: Es gibt eine bestimmte Methode (etwas mit .keys), 
#    mit der du dir nur die Schlüsselwörter (Namen der Waffen) eines Dictionaries ausgeben lassen kannst. 
#    Versuche, das mit print() auf dem Bildschirm auszugeben!

# 2. Frage den Spieler per input(), welche Waffe aus der Liste er verbessern will.

# 3. Prüfe, ob die Eingabe (der Key) im Dictionary 'waffen_schaden' existiert.
#    - Wenn JA: Greife gezielt auf DIESEN EINEN Key zu und erhöhe seinen Wert um 5. 
#               Gib danach einen coolen Spruch per print() aus (z.B. "Dein Schwert leuchtet auf!").
#    - Wenn NEIN: Lass den Schmied wieder einen schönen Spruch drücken 
#                 (z.B. "Sowas schmiede ich nicht, du Banane!").

# --- DEINE AUFGABE ENDE ---



print("Deine Waffen machen jetzt so viel Schaden:", waffen_schaden)