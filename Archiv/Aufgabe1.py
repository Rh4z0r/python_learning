zahl = int(input("bitte eine zahl eingeben"))
while zahl % 2 == 0:
   zahl = int(input("bitte eine weitere Zahl eingeben"))
   print(f"Eingegebene Zahl: {zahl}")

print(f"Die Zahl {zahl} ist ungerade! Das Programm wird beendet.")
