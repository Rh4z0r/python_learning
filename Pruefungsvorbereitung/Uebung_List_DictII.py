# Eine Liste von Dictionaries. Jedes Dictionary ist ein tierischer Patient.

patienten = [
    {"name": "Bello", "tierart": "Hund", "alter": 4},
    {"name": "Mimi", "tierart": "Katze", "alter": 2},
    {"name": "Rex", "tierart": "Hund", "alter": 8},
    {"name": "Nemo", "tierart": "Fisch", "alter": 1},
    {"name": "Luna", "tierart": "Katze", "alter": 5}
]

preisliste = {
    "Impfung": 45,
    "Wurmkur": 15,
    "Krallen schneiden": 10,
    "Checkup": 30
}

def finde_tiere(patienten_liste, gesuchte_art):
    ergebnis_liste = [] # Wieder: besser nicht 'liste' nennen 😉
    
    for item in patienten_liste:
        # Wir prüfen das Etikett "tierart" im aktuellen Dictionary
        if item["tierart"] == gesuchte_art: 
            # Wenn es passt, hängen wir nur das Etikett "name" an
            ergebnis_liste.append(item["name"]) 
            
    return ergebnis_liste

print(finde_tiere(patienten, "Hund"))       

def berechne_rechnung(behandlungs_liste, preise_dict):
    summe = 0
    for teil in behandlungs_liste:
        preis = preisliste[teil]
        summe += preis
    return summe

print(berechne_rechnung(["Checkup", "Wurmkur"], preisliste))
