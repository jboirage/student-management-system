#Define Student class that inherits from Person - student.py
from person import Person

class Student(Person):
    def __init__(self, student_id, name):
        """
        Initialize a Student object.

        Parameters:
        - student_id (str): The unique identifier for the student.
        - name (str): The name of the student.
        """
        self.student_id = student_id
        self.name = name
        self.courses = {}
        self.enrolled_courses = []  #Track enrolled courses in a list for quick access


    def enroll_in_course(self, course):
        """
        Enroll the student in a course.

        Parameters:
        - course (Course): The course object to enroll in.
        """ 
        #Call the add_student method of the Course class to track the student in the course
        course.add_student(self) 
        
        #Track the enrolled courses in the Student class to quickly access enrolled courses
        self.enrolled_courses.append(course)

        #Note: Tracking enrolled courses in both the Course class and the Student class
        #allows for efficient retrieval of information from both perspectives.
        #The Course class can quickly access enrolled students,
        #while the Student class can easily access the courses in which the student is enrolled.

    def __str__(self):
        """String representation of the Student object."""
        return f"Student ID: {self.student_id}, Name: {self.name}"
    
    def view_grades(self):
        """Display the grades of the student in enrolled courses."""
        for course_code, course in self.courses.items():
            grade = course.grades.get(self.student_id, "N/A")
            print(f"Course: {course_code}, Grade: {grade}")

    def display_info(self):
        """Display information about the student."""
        print(f"Student ID: {self.student_id}, Name: {self.name}")
