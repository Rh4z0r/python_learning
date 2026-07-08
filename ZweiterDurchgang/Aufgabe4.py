temps = [18, 21, 22, 18, 20, 21, 18, 19]
minimum = temps[0]
maximum = temps[0]
summe = 0 
anzahl = 0 


for v in temps:
    if v < minimum:
        minimum = v
    if v > maximum:
        maximum = v
                                
summe += v
anzahl += 1

durchschnitt = summe/anzahl

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Durchschnitt: {durchschnitt}")