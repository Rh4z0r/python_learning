try: 
    hoehe = int(input("Geben sie die gewünschte  Höhe des Dreiecks ein: "))
    zeichen ="#"

    for i in range(1, hoehe + 1):
        print(zeichen * i) 

    for i in range(hoehe - 1, -10, -1):
        print(zeichen * i)

except ValueError: 
    print("gib eine richtige Zahl ein du penner")