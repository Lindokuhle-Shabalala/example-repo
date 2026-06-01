# Must read the data from txt file
with open('DOB.txt', 'r', encoding='utf-8') as file:
    names = []
    dates_of_birth = []

    for line in file:
        splitted_lines = line.split()
        names.append(splitted_lines[:2])
        dates_of_birth.append(splitted_lines[2:])

# Print section header for names
print("Name\n")
for name in names:
    print(" ".join(name))

# Print section header for dates of birth
print("\nBirth Date\n")
for dob in dates_of_birth:
    print(" ".join(dob))