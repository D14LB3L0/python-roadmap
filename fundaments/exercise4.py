students = []

def main():
    while True:
        try:
            option = int(input(
                "1. Add student\n"
                "2. Show students\n"
                "3. Leave\n"
            ))
            if int(option) == 1:
                add_student()
            elif int(option) == 2:
                show_students()
            elif int(option) == 3:
                print("Exiting the program.")    
                break
        except ValueError:
            print("Please enter a valid option.")
            continue


def add_student():
    grades =  []
    
    while True:
        try:
            grade = ""
            
            name = input("Enter the student's name: ")
            for i in range(3):
                while True:
                    grade = input("Enter the student's grades: ")
                    if not grade.isdigit() or int(grade) < 0 or int(grade) > 20:
                        print("Please enter a valid grade (0 - 20)")
                        continue
                    grades.append(int(grade))
                    break
            
            average = sum(grades)/len(grades) if grades else 0
            students.append({
                "name": name,
                "grade": grades,
                "average": average
            })
            break
        except ValueError:
            print("Please enter valid data.")
            continue
        

def show_students():
    for student in students:
        if student['average'] >= 12:
            aprove = "Approved"
        else:
            aprove = "Not Approved"
        
        print(f"Name: {student['name']}, Grades: {student['grade']}, Average: {student['average']:.2f}, Status: {aprove}")
        
main()    





