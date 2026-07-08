film_titel = [
    "Inception", 
    "Avatar", 
    "Joker", 
    "Titanic", 
    "Matrix", 
    "Alien", 
    "Gladiator",
    "Up"
]

film_bewertungen = {
    "Inception": 88,
    "Avatar": 79,
    "Joker": 84,
    "Titanic": 89,
    "Matrix": 87,
    "Alien": 85,
    "Gladiator": 85,
    "Up": 82
}

def finde_kurze_titel(titel_liste, max_laenge):
    list = []
    for titel in titel_liste:
        if len(titel) <= max_laenge:
            list.append(titel)
    return list

ergebnis = finde_kurze_titel(film_titel, 3)

print(ergebnis)


def finde_top_filme(bewertungs_dict, min_bewertung):
    list = []
    for item in bewertungs_dict:
        bewertung = bewertungs_dict[item]
        if bewertung >= min_bewertung:
            list.append(item)
    return list
print(finde_top_filme(film_bewertungen, 84))