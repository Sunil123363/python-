class Student():
    def __init__(self, Student_id, name, roll_num, Identification, Branch, total_marks, grade_to_total_marks):
        self.Student_id = Student_id
        self.name = name
        self.roll_num = roll_num
        self.Identification = Identification
        self.Branch = Branch
        self.total_marks = total_marks
        self.grade_to_total_marks = grade_to_total_marks

    def out_details(self):
        return f"Student_id : {self.Student_id} \n Name :{self.name} \n Roll_num:{self.roll_num}  \n IDentificaton:{self.IDentification} \n Branch:{self.Branch} \n total_marks:{self.total_marks} \ngrade_total_marks:{self.grade_to_total_marks}"


class Option_functions():
    def __init__(self):
        self.students = []

    def include_student(self, student):
        self.students.append(student)

    def remove_student(self, Student_id):
        for student in self.students:
            if student.Student_id == Student_id:
                self.students.remove(student)
                return True
        return False

    def Find_student(self, Student_id):
        for student in self.students:
            if student.student_id == Student_id:
                return student
        return None

    def update_student(self, Student_id, name, roll_num, grade_to_total_marks, Identification, Branch):
        student = self.Find_student(Student_id)
        if student:
            student.Student_id = Student_id
            student.name = name
            student.Identification = Identification
            student.grade_to_total_marks = grade_to_total_marks
            student.roll_num = roll_num
            student.Branch = Branch
            return True
        return False

    def get_student_count(self):
        return len(self.students)

    def list_students(self):
        if not self.students:
            return "No students in the list."
        student_details = ""
        for student in self.students:
            student_details += student.out_details() + "\n"
        return student_details


def Details_menu():
    print("Enter the number attached to the menu item to get the outcomes!")
    print("1.Add student to the list:")
    print("2.Remove student from the list :")
    print("3.Find the student")
    print("4.Update the student details:")
    print("5.find the total number of students")
    print("6.find all the student details:")
    print("10.exit")


def main():
    cse = Option_functions()
    while True:
        Details_menu()
        choice = input('Choose one form (1-9)')

        if choice == '1':
            Student_id = input("enter your student id:")
            name = input('enter your name:')
            roll_num = input('enter your roll_number:')
            Identification = input('enter any identification mark:')
            Branch = input("enter your branch:")
            total_marks = input("enter the total_marks obtained :")
            grade_to_total_marks = True
            Std = Student(Student_id, name, roll_num, Identification,
                          Branch, total_marks, grade_to_total_marks)
            cse.include_student(Std)
            print('Data added*')

        elif choice == "2":
            Student_id = input("Enter student id to remove: ")
            if cse.remove_student(Student_id):
                print("Student removed*")
            else:
                print("Student not found.")

        elif choice == "3":
            Student_id = input("Enter student id to find: ")
            student = cse.Find_student(Student_id)
            if student:
                print(student.get_details())
            else:
                print("Student not found.")

        elif choice == "4":
            Student_id = input("enter student ID to update: ")
            name = input("enter your name: ")
            roll_num = input("enter your roll_number:")
            Identification = input('enter any identification mark:')
            Branch = input("enter your branch:")
            total_marks = input("enter the total_marks obtained :")
            grade_to_total_marks = True

            if cse.update_student(Student_id, name, roll_num, grade_to_total_marks, Identification, Branch):
                print("Student details updated successfully!")
            else:
                print("Student not found.")

        elif choice == "5":
            print(f"Total number of students: {cse.get_student_count()}")

        elif choice == "6":
            print(cse.list_students())


if __name__ == "__main__":
    main()
