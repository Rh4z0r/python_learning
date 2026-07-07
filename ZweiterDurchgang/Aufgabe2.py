names = [ "Liam", "Olivia", "Noah", "Charlotte", "Oliver", "Emma", "Theodore", "Amelia", "Henry", "Sophia", "James", "Mia", "Elijah", "Isabella", "Mateo", "Evelyn", "William", "Sofia", "Lucas", "Eliana" ]
sortnames = []

def sort(unsortiert):
    sortiert = sorted(unsortiert)
    sortnames.extend(sortiert)
    
sort(names)

print(sortnames)
