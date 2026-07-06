# ==========================================
# Aufgabe 6: Umrechnen von bin/hex/dec
# =========================================

print("Willkommen beim Zahlenumwandler. Bitte wählen Sie, was Sie tun möchten:")
print("für Dezimal ->  Hexadezimal drücken Sie die [1]")
print("für Dezimal ->  Binär drücken Sie die [2]")
print("für Binär ->  Dezimal drücken Sie die [3]")
print("für Binär -> Hexadezimal drücken Sie die [4]")
print("für Hexadezimal ->  Dezimal drücken Sie die [5]")
print("für Hexadezimal -> Binär drücken Sie die [6]")

aktion = input("Deine Wahl: ")

if aktion == "1":
    meine_zahl = int(input("Bitte geben Sie eine Dezimal-Zahl ein und ich wandle sie in Hexadezimal um: "))
    hexa_ergebnis = hex(meine_zahl)
    print("Das Ergebnis ist", hexa_ergebnis)

if aktion == "2":
    meine_zahl = int(input("Bitte geben Sie eine Dezimal-Zahl ein und ich wandle sie in eine Binärzahl um: "))
    bin_ergebnis = bin(meine_zahl)
    print("Das Ergebnis ist", bin_ergebnis)

if aktion == "3":
    # Hier kein int() beim input, wir brauchen den Text (String)
    meine_zahl = input("Bitte geben Sie eine Binär-Zahl ein und ich wandle sie in Dezimal-Zahl um: ")
    dez_ergebnis = int(meine_zahl, 2)
    print("Das Ergebnis ist", dez_ergebnis)
    
if aktion == "4":
    meine_zahl = input("Bitte geben Sie eine Binär-Zahl ein und ich wandle sie in Hexadezimal um: ")
    hexa_ergebnis = hex(int(meine_zahl, 2))
    print("Das Ergebnis ist", hexa_ergebnis)    
    
if aktion == "5":
    meine_zahl = input("Bitte geben Sie eine Hexadezimal-Zahl ein und ich wandle sie in Dezimalzahl um: ")
    dez_ergebnis = int(meine_zahl, 16)
    print("Das Ergebnis ist", dez_ergebnis)
    
if aktion == "6":
    meine_zahl = input("Bitte geben Sie eine Hexadezimal-Zahl ein und ich wandle sie in Binär-Zahl um: ")
    bin_ergebnis = bin(int(meine_zahl, 16)) 
    print("Das Ergebnis ist", bin_ergebnis)