import numpy as np

strecke = [0, 10, 40, 90, 160]

geschwindigkeit = np.gradient(strecke)
print("Geschwindigkeiten (Ableitung):", geschwindigkeit)

# ==========================================
# INTEGRIEREN (Update für neuere NumPy Versionen)
# ==========================================
# trapz heißt jetzt trapezoid!
gesamt_strecke = np.trapezoid(geschwindigkeit)

print("Integrierte Gesamtstrecke:", gesamt_strecke)