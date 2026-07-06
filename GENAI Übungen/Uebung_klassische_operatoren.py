import statistics

# Unsere Liste mit Messwerten
werte = [12, 4, 88, 4, 15, 22, 4]

# 1. min() und max() - direkt in Python eingebaut
kleinster_wert = min(werte)
groesster_wert = max(werte)

# 2. mean() - Der mathematische Durchschnitt (Alle addieren / Anzahl)
durchschnitt = statistics.mean(werte)

# 3. median() - Der Wert genau in der Mitte, wenn man die Liste sortiert
# (Super nützlich, weil er sich von extremen Ausreißern wie der 88 nicht ablenken lässt!)
mitte = statistics.median(werte)

print(f"Min: {kleinster_wert}, Max: {groesster_wert}")
print(f"Durchschnitt: {durchschnitt:.2f}") # .2f rundet auf zwei Nachkommastellen
print(f"Median: {mitte}")