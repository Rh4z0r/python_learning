meine_scores = [150, 420, 90, 500, 300, 50]

def filter_top_scores(scores, min_score):
    score = []
    for item in scores: 
        if item >= min_score:
             score.append(item)
    return score
               
    
# Die Funktion sollte hier [420, 500, 300] zurückgeben
ergebnis = filter_top_scores(meine_scores, 300)

mein_warenkorb = [
    {"name": "Apfel", "kategorie": "Obst", "preis": 1.50},
    {"name": "Milch", "kategorie": "Milchprodukte", "preis": 1.20},
    {"name": "Banane", "kategorie": "Obst", "preis": 2.00},
    {"name": "Käse", "kategorie": "Milchprodukte", "preis": 3.50},
    {"name": "Brot", "kategorie": "Backwaren", "preis": 2.50}
]

def berechne_kategorie_kosten(warenkorb):
    # 1. Unser leeres Sammel-Gefäß
    kategorie_kosten = {} 

    # 2. Wir schauen uns jeden Artikel im Warenkorb einzeln an
    for artikel in warenkorb: 
        
        # 3. Wir holen uns die Infos aus dem aktuellen Artikel-Dictionary
        aktuelle_kategorie = artikel["kategorie"]
        aktueller_preis = artikel["preis"]

        # 4. Die Weiche: Kennen wir die Kategorie schon?
        if aktuelle_kategorie in kategorie_kosten:
            # JA! Wir addieren den Preis auf den bestehenden Wert obendrauf
            kategorie_kosten[aktuelle_kategorie] += aktueller_preis
        else:
            # NEIN! Wir legen den Eintrag im Dictionary ganz neu an
            kategorie_kosten[aktuelle_kategorie] = aktueller_preis
            
    # 5. Fertiges Dictionary zurückgeben
    return kategorie_kosten

ergebnis = berechne_kategorie_kosten(mein_warenkorb)
print(ergebnis)