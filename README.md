# Student_Note_Program
This is a student note program. This program uses phyton. It can save data by json. You can save your lessons and points. It also can caculate the averange of the lesson points. 

# Student Management System (Python CLI)

A simple yet effective Command Line Interface (CLI) application built with Python. This project was developed as a practical exercise to master fundamental programming concepts such as **Data Structures**, **File I/O**, and **Modular Programming**.

## 🚀 Features
- **Course Management:** Add and remove lessons dynamically.
- **Grade Tracking:** Add multiple scores for each lesson.
- **Academic Statistics:** Calculate individual lesson averages and overall GPA.
- **Attendance Tracking:** Keep track of student absenteeism.
- **Persistent Storage:** Data is automatically saved to and loaded from a `school_data.json` file.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Format:** JSON (for persistent storage)

## 📸 How It Works
The program uses a dictionary-based data structure where each lesson acts as a key, and its scores are stored in a list:
```python
"lessons": {
    "Mathematics": [85, 90, 78],
    "Physics": [70, 88]
}
