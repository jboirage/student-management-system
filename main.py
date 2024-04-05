#Define main function for sample usage of the Student Management System - main.py 
from student import Student
from course import Course

def main():
    """Sample of Student Management System."""
    #Sample usage of the Student Management System
    student1 = Student(student_id="T301", name="Bob") #User can change the student name and ID
    student2 = Student(student_id="T240", name="Kevin") #User can change the student name and ID

    course1 = Course(course_code="M120", name="Algebra") #User can change course name
    course2 = Course(course_code="S150", name="Biology") #User can change course name

    #Enrolling students in courses
    student1.enroll_in_course(course1)
    student2.enroll_in_course(course2)

    #Assigning grades
    course1.assign_grade(student1, grade= "A") #User can change grade letter
    course2.assign_grade(student2, grade= "B") #User can change grade letter

    #Display student information
    print("\n")    
    student1.display_info()
    student1.view_grades()
    
    student2.display_info()
    student2.view_grades()

    #Generate course reports
    print("\n")    
    print(course1.generate_report())   
    print(course2.generate_report())

if __name__ == "__main__":
    main()