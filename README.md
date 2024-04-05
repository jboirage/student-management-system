# Student Management System - Created by Jaden Boiragee

## Overview

This is a simple Student Management System implemented in Python. It allows users to manage student information, courses, enrollments, and grades.

## How to Run the Program

### 1. Download the Code

- Download the Python script files (`main.py`, `student.py`, `course.py`, `person.py`) to a directory of your choice.

### 2. Run the Program

- Open a new terminal or command prompt.
- Navigate to the directory where the script files are located.
- Run the program by executing the command: 
    ```
    python main.py
    ```
    or 
    ```
    python3 main.py
    ```

### 3. Customization

You have the flexibility to customize various aspects of the program:

- **Student Information**: In `main.py`, you can modify the `student_id` and `name` parameters when creating instances of the `Student` class.
- **Course Information**: Similarly in `main.py`, you can customize the `course_code` and `name` parameters when creating instances of the `Course` class.
- **Grade Assignment**: Modify the `grade` parameter in the `assign_grade` method in `main.py` to assign different grades.

### 4. Executing the Program

- Once the customization is complete, save the changes in the code.
- Return to the terminal or command prompt.
- Run the program again using the command: 
    ```
    python main.py
    ```
    or 
    ```
    python3 main.py
    ```

### 5. Running Unit Tests

To check that the Student Management System is working correctly, unit tests have been included. These tests verify different functionalities, such as enrolling students, assigning grades, and generating reports.

#### Prerequisites:

1. **Python Installed**: Make sure that Python is installed.
2. **pytest Package**: Make sure `pytest` package is installed: 
    ```
    pip install pytest
    ```

#### Steps to Run the Tests:

1. **Navigate to the Project Directory**:
   - Open a terminal or command prompt and navigate to the directory where your project files are located.

2. **Run the Tests**:
   - Execute the following command to run the unit tests:
     ```
     pytest test_student_management_system.py
     ```

3. **View Test Results**:
   - After running the tests, the terminal will display the test results.

4. **Interpreting Results**:
   - If all tests pass, there will be a message indicating the number of tests passed.
   - If there are failures, there will be a message indicating the number of tests that didn’t pass.

Feel free to experiment with different student details, courses, and grades!

Thank you for using the Student Management System! :)


