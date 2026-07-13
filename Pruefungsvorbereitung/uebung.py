name_popularity = {
    "Harper": 91, 
    "Elijah": 97, 
    "Zoe": 76, 
    "Henry": 88, 
    "Alexander": 95
}

names = ["Harper", "Elijah", "Zoe", "Henry", "Alexander"]

def filter_by_popularity(names, min_pop):
    result = []
    for name in names:
        pop = name_popularity.get(name, 0)
        if pop >= min_pop:
            result.append(name)
    return result

print(filter_by_popularity(names, 90))