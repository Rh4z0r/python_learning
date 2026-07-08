# integration

import math

data = [1.2, 5.66, 4.58, 7.5, 1.0]

sample_rate = 0.1

def cal_integral(data):
    integral = 0
    for i in range(1, len(data)):
        height = 0.5 *(data[i] + data[i - 1])
        integral += height / sample_rate    
    return integral
print(cal_integral(data))

# differentierung

data = [1.2, 5.66, 4.58, 7.5, 1.0] # Unsere Messwerte
sample_rate = 0.1 # Unser Abstand (Delta x bzw. Delta t)

def cal_derivative(data):
    ableitungen = [] # Eine leere Liste, um die Steigungen zu sammeln
    
    # Wir iterieren nur bis zum VORLETZTEN Element (len(data) - 1),
    # da wir für die Steigung immer den Punkt i und den NÄCHSTEN Punkt (i+1) brauchen.
    for i in range(len(data) - 1):
        # Die klassische Formel: (y_neu - y_alt) / Delta_x
        steigung = (data[i + 1] - data[i]) / sample_rate
        ableitungen.append(steigung)
        
    return ableitungen

print(cal_derivative(data))