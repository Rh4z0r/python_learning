stimmen = {
    "Hund": 5,
    "Katze": 3,
    "Hamster": 1
}

# Jemand gibt seine Stimme ab
neues_tier = input("Für welches Tier möchtest du abstimmen? ")

if neues_tier in stimmen: 
    stimmen[neues_tier] += 1
else: 
    stimmen[neues_tier] = 1


print("Aktueller Stand der Abstimmung:", stimmen)