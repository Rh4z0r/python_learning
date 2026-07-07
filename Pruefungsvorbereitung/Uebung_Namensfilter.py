names = [
    "Emma", 
    "Liam", 
    "Olivia", 
    "Noah", 
    "Sophia",
    "Mason", 
    "Isabella", 
    "James", 
    "Ava", 
    "Lucas", 
    "Mia", 
    "Ethan", 
    "Charlotte", 
    "Benjamin", 
    "Amelia"
]

name_popularity = {
    "Harper": 91,
    "Elijah": 97,
    "Zoe":76,
    "Henry":88,
    "Lily":83, 
    "Alexander":95,
    "Grace":72,
    "Daniel":86,
    "Chloe":80,
    "Jack":89, 
    "Scarlett":84,
    "Sebastian":93, 
    "Nora":78,
    "Samuel":81, 
    "Victoria":87,
    }



def filter_by_num_of_char(list, num_of_characters):
    filtered_list = []
    for item in list:
        if len(item) <= num_of_characters:
            filtered_list.append(item)
    return filtered_list

def filter_by_popularity(list, pupularity):
    filtered_list = []
    for item in list:
        popularity_of_name = name_popularity[item]
        if popularity_of_name >= popularity:
            filteres_list.append(item)
            
    return filtered_list
 
popularity = name_popularity["Harper"]    

print(filter_by_num_of_char(names, 3))
print(filter_by_num_of_char(names, 6))
print(filter_by_num_of_char(names, 1))
print(filter_by_num_of_char(names, 7))
print(filter_by_num_of_char(names, 8))    
print(popularity)