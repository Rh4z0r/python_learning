values = [21, 22, 23, -999, 20, 19, -999, 18]
true = [0]

def getMaxValue(values):
    for v in values:
        if v > 0:
            true.append(v)
        
    return

getMaxValue(values)

print(true)