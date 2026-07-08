import tkinter as tk
from tkinter import simpledialog

# Das leere Hauptfenster im Hintergrund verstecken
root = tk.Tk()
root.withdraw()

# Den Input-Dialog anzeigen
antwort = simpledialog.askstring("Titel des Fensters", "Was möchtest du mir sagen?")

# Das Ergebnis verarbeiten
if antwort is not None:
    print(f"Deine Eingabe war: {antwort} 🎉")
else:
    print("Du hast auf Abbrechen geklickt! 🙈")