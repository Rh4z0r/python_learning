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


# 1. Finde kurze Titel mit einer maximalen Zeichenzahl von 3
# 2. Finde top Filmbewertungen über 80
 
tl = []

def finde_kurze_titel(titel):
    for titel in film_titel:
        if len(titel) <= 3:
            tl.append(titel)

    return tl

print(finde_kurze_titel(tl))



def finde_top_bewertungen(bewertungs_dict):
    bw = []
    for name, bewertung in bewertungs_dict.items():
        if bewertung >  80: 
            bw.append(name)
    return bw

print(finde_top_bewertungen(film_bewertungen))


