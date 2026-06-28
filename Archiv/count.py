def getMaxValue(values):
    aktuelles_maximum = values[0]
    for zahl in values:
        if abs(zahl) > abs(aktuelles_maximum):
            aktuelles_maximum = zahl
    return aktuelles_maximum

values = [21, 22, 23, -999, 20, 19, -999, 18]
ergebnis = getMaxValue(values)
print(f"Die größte Zahl ist: {ergebnis}")