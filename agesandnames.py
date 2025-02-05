people = []
for i in range(5):
    name = input(f"Enter name for person {i+1}: ")
    while True:
        age = input(f"Enter age for {name}: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid age. Please enter a valid number.")
    people.append([name, age])

people.sort(key=lambda x: x[1])

print("\nPeople sorted by age (from younger to older):")

for person in people:
    print(f"{person[0]} - {person[1]} years old")
#ALLAGH GIA TO GITHUB NEO BRANCH
