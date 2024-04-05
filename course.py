#Define Course class - course.py
class Course:
    def __init__(self, course_code, name):
        """
        Initialize a Course object.

        Parameters:
        - course_code (str): The unique identifier for the course.
        - name (str): Name of course.
        """
        self.course_code = course_code
        self.name = name
        self.enrolled_students = {} #Track enrolled students in a dictionary for quick access
        self.grades = {} #Dictionary to store student grades

    def add_student(self, student):
        """
        Add a student to the enrolled students of the course.

        Parameters:
        - student (Student): The student object to add to the course.
        """
        self.enrolled_students[student.student_id] = student
    
    def assign_grade(self, student, grade):
        """
        Assign a grade to a student in the course.

        Parameters:
        - student (Student): The student object to assign a grade to.
        - grade (str): The grade to assign to the student.
        """
        self.grades[student.student_id] = grade
    
    def generate_report(self):
        """Generate a report for the course, displaying student grades."""
        report = f"Enrolled students in {self.name}:\n"
        
        if not self.enrolled_students:
            report += "No students enrolled in this course.\n"
        else:
            for student_id, student in self.enrolled_students.items():
                grade = self.grades.get(student_id, "N/A")
                report += f"{student}\n"
                report += f"Course: {self.course_code}, Grade: {grade}\n"

        return report

    def __str__(self):
        """String representation of the Course object."""
        return f"Course: {self.course_code}, Name: {self.name}"
