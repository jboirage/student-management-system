#Import the modules
import pytest
from main import Student, Course

#Unit tests for the Student Management System

def test_enroll_student_in_course():
    """Test enrolling a student in a course."""
    #Arrange
    student = Student(student_id="T301", name="Bob")
    course = Course(course_code="M120", name="Algebra")

    #Act
    student.enroll_in_course(course)

    #Assert
    assert student.enrolled_courses == [course]
    assert course.enrolled_students == {"T301": student}

def test_generate_report_no_students(capsys):
    """Test generating a report when no students are enrolled."""
    #Arrange
    course = Course(course_code="M120", name="Algebra")

    #Act
    report = course.generate_report()

    #Assert
    assert "No students enrolled in this course." in report

def test_generate_report_with_students(capsys):
    """Test generating a report with enrolled students."""
    #Arrange
    student = Student(student_id="T301", name="Bob")
    course = Course(course_code="M120", name="Algebra")

    #Act
    student.enroll_in_course(course)
    course.assign_grade(student, grade="A")
    report = course.generate_report()

    #Assert
    assert "Enrolled students in Algebra:" in report
    assert "Course: M120, Grade: A" in report