names = ["Γιωργος Παπαδοπουλος", "Μαρια Τζημα", "Γρηγορης Μπαλτας", "Λουκια Αλυρα"]
incomes = [1200, 1500, 1300, 1100]

max_income = incomes.index(max(incomes))
person_with_max_income = names[max_income]

min_income = incomes.index(min(incomes))
person_with_min_income = names[min_income]

total_income = sum(incomes)
avg_income = total_income / len(incomes)

print("List of people and their incomes:")
print(", ".join([f"[{name}, {income} euros]" for name, income in zip(names, incomes)]))

print(f"\nPerson with the highest income: {person_with_max_income} ({max(incomes)} euros)")
print(f"Person with the lowest income: {person_with_min_income} ({min(incomes)} euros)")

print(f"\nAverage income: {avg_income:.2f} euros")
print(f"Total income: {total_income:.2f} euros")

print("\nPercentage of each person's income relative to the average income:")
for name, income in zip(names, incomes):
    percentage_of_average = (income / avg_income) * 100
    print(f"{name}: {percentage_of_average:.2f}%")
