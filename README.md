# EduManage

EduManage is a Python-based education management system designed to handle student, lecturer, and lecture data efficiently. It simplifies administrative tasks, making it easier to manage enrollments and personal data.

## Features

- **Student Management**: Add, update, and retrieve student records.
- **Lecturer Management**: Manage lecturer profiles and assignments.
- **Lecture Enrollment**: Enroll students in lectures and manage lecture details.
- **Data Storage**: Store lecture and user information in CSV format.

## Project Structure

```plaintext
EduManage/
│
├── enrollment.py        # Logic for handling student enrollment
├── lecture.py           # Lecture structure and details
├── lecture_list.py      # Manages the lecture list
├── lecturer.py          # Lecturer details
├── lecturer_list.py     # Manages the lecturer list
├── person.py            # Common attributes for students and lecturers
├── student.py           # Student-specific details
├── student_list.py      # Manages the student list
├── lecture_list.csv     # CSV file for storing lectures
├── main.py              # Entry point for the application
└── README.md            # Project overview and instructions

 
