while True:
    try:
        zahl = int(input("Bitte gib eine Zahl ein, ich prüfe ob sie gerade oder ungerade ist: "))
    

        if zahl % 2 == 1: 
        
            print("Du hast eine ungerade Zahl eingegeben...")
            
            break
        
        else: 
            print("Versuche es nochmal, das war eine gerade Zahl. ")

    except ValueError: 

        print("Bitte gib eine Zahl ein und nichts anderes...")
