import json
students = {}
def add_student(name):
    """Creates a new student entry if they don't already exist"""
    if name not in students:
        students[name] = {}
        print(f"Added student: {name}")
    else:
        print(f"{name} already exists.")

def add_subject(student_name,subject_name):
    """Add a subject under a student."""
    if student_name not in students:
        print(f"{student_name} doesnot exist. Please add the student first")
        return
    if subject_name not in students:
        students[student_name][subject_name] = []
        print(f"Added subject '{subject_name}' for {student_name}")
    else:
        print(f"{subject_name} already exists for {student_name}")

def add_assignment(student_name,subject_name,assignment_name,score,weight):
    """ Add one graded assignment to a subject."""
    if student_name not in students:
        print(f" {student_name} not found.")
        return
    if subject_name not in students[student_name]:
        print(f" {subject_name} not found for {student_name}.")
        return
    assignment = {
        "name": assignment_name,
        "score": score,
        "weight": weight
    }
    students[student_name][subject_name].append(assignment)
    print(f" Added '{assignment_name}' ({score}%, weight {weight} to {subject_name}")

def calculate_subject_average(student_name,subject_name):
    """Calculate the weighted average for one subject."""
    if student_name not in students:
        print(f"{student_name} not found.")
        return None
    if subject_name not in students[student_name]:
        print(f"{subject_name} not found for {student_name}.")
        return None
    assignments = students[student_name][subject_name]
    if not assignments:
        print(f"No assignments yet for {subject_name}.")
        return None
    total = 0
    for assignment in assignments:
        total += assignment["score"]*assignment["weight"]
    return total

def calculate_overall_average(student_name):
    """Calculate a student's overall average across all subjects."""
    if student_name not in students:
        print(f"{student_name} not found.")
        return None
    subjects = students[student_name]
    if not subjects:
        print(f"{student_name} has no subjects yet.")
        return None
    subject_averages = []
    for subject_name in subjects:
        avg = calculate_subject_average(student_name,subject_name)
        if avg is not None:
            subject_averages.append(avg)
    if not subject_averages:
        return None
    overall = sum(subject_averages) / len(subject_averages)
    return overall

def get_letter_grade(average):
    """Convert a numeric average into a letter grade."""
    if average is None:
        return "N/A"
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def save_data(filename="grades.json"):
    """Save the students dictionary to a JSON file."""
    with open(filename, "w") as file:
        json.dump(students,file,indent=4)
    print(f"Data saved to {filename}")

def load_data(filename="grades.json"):
    """Load the students dictionary fron a JSON file,if it exists."""
    global students
    try:
        with open(filename, "r") as file:
            students = json.load(file)
        print(f"Data loaded from {filename}")
    except FileNotFoundError:
        print(f"No saved data found.starting fresh.")

def main_menu():
    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Add Assignment")
        print("4. View Subject Average")
        print("5. View Overall Average & Grade")
        print("6. View All Students")
        print("7. Save & Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)
        elif choice == "2":
            name = input("Enter student name: ")
            subject = input("Enter subject name: ")
            add_subject(name, subject)
        elif choice == "3":
            name = input("Enter student name: ")
            subject = input("Enter subject name: ")
            assignment_name = input("Enter assignment name: ")
            score = float(input("Enter score: "))
            weight = float(input("Enter weight (e.g. 0.4 for 40%): "))
            add_assignment(name, subject, assignment_name, score, weight)
        elif choice == "4":
            name = input("Enter student name: ")
            subject = input("Enter subject name: ")
            avg = calculate_subject_average(name, subject)
            grade = get_letter_grade(avg)
            print(f"{name}'s {subject} average: {avg} ({grade})")
        elif choice == "5":
            name = input("Enter student name: ")
            avg = calculate_overall_average(name)
            grade = get_letter_grade(avg)
            print(f"{name}'s overall average: {avg} ({grade})")
        elif choice == "6":
            print(students)
        elif choice == "7":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

load_data()
main_menu()



    