import random

students = []
stoixeia = {
    "Ονομα": "",
    "Εκθεση": "",
    "Μαθηματικα": "",
    "Φυσικη": "",
    "Χημεια": ""
}
#ta stoixeia pio panw
#
#
#dhlwnw stoixeia ma8htwn edw
def enter_student_data():
    while True:
        name = input("Δώσε ονοματεπώνυμο μαθητή (ή '@' για έξοδο): ")
        if name == "@":
            break
        grades = {}
        for subject in ["Εκθεση","Μαθηματικά", "Φυσική", "Χημεία", "Βιολογία"]:
            grades[subject] = random.randint(1, 20)
        student = {"Ονοματεπώνυμο": name, "Βαθμοί": grades}
        students.append(student)

        stoixeia["Ονομα"] = name
        stoixeia["Εκθεση"] = random.choice(["Εκθεση"])
        stoixeia["Μαθηματικα"] = grades["Μαθηματικά"]
        stoixeia["Φυσικη"] = grades["Φυσική"]
        stoixeia["Χημεια"] = grades["Χημεία"]

def display_students():
    for student in students:
        print(f"Μαθητής: {student['Ονοματεπώνυμο']}")
        for subject, grade in student['Βαθμοί'].items():
            print(f"  {subject}: {grade}")

def display_student_grade():
    name = input("Δώσε ονοματεπώνυμο μαθητή: ")
    subject = input("Δώσε όνομα μαθήματος: ")
    for student in students:
        if student['Ονοματεπώνυμο'] == name:
            if subject in student['Βαθμοί']:
                print(f"Ο βαθμός του/της {name} στο μάθημα {subject} είναι: {student['Βαθμοί'][subject]}")
            else:
                print(f"Ο/Η {name} δεν έχει βαθμό στο μάθημα {subject}")
            return
    print(f"Ο/Η {name} δεν βρέθηκε στη λίστα μαθητών")

def average_grade_for_subject(subject):
    total_grades = 0
    count = 0
    for student in students:
        if subject in student['Βαθμοί']:
            total_grades += student['Βαθμοί'][subject]
            count += 1
    if count > 0:
        average = total_grades / count
        print(f"Ο μέσος όρος για το μάθημα {subject} είναι: {average}")
    else:
        print(f"Δεν υπάρχουν βαθμοί για το μάθημα {subject}")

def average_grades_per_student():
    for student in students:
        total_grades = sum(student['Βαθμοί'].values())
        num_subjects = len(student['Βαθμοί'])
        average = total_grades / num_subjects
        print(f"Ο μέσος όρος του/της {student['Ονοματεπώνυμο']} είναι: {average:.2f}")

enter_student_data()
print("\nΛίστα Μαθητών:")
display_students()

#print("\nΜέσος όρος ανά μάθημα:")
#for subject in ["Μαθηματικά", "Φυσική", "Χημεία", "Βιολογία"]:
#    average_grade_for_subject(subject)

    


#print("\nΜέσος όρος ανά μαθητή:")
#average_grades_per_student()

#display_student_grade()  
#print("\nΣτοιχεία τελευταίου μαθητή που προστέθηκε:")
#for key, value in stoixeia.items():
#    print(f"{key}: {value}")
