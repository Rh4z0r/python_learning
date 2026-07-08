def dummy_training(dummy_hp):
    print("Das Training beginnt! ⚔️")

    while dummy_hp > 0: 
        dummy_hp -= 1
        print(f"Zack! Dummy noch {dummy_hp} HP übrig.")

     

       

    # --- DEINE AUFGABE START ---
    
    # 1. Erstelle eine while-Schleife, die läuft, SOLANGE 'dummy_hp' größer als 0 ist.
    # 2. Ziehe in jedem Durchlauf der Schleife 1 von 'dummy_hp' ab (-= 1).
    # 3. Gib in jedem Durchlauf per print() aus: f"Zack! Dummy hat noch {dummy_hp} HP übrig."
    
    # --- DEINE AUFGABE ENDE ---
    
    print("Der Dummy ist kaputt! Training beendet. 🏆")

# Hier rufen wir die Funktion auf und geben dem Dummy 5 HP:
dummy_training(5)