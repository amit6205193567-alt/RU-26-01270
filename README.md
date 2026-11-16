# Hospital Management System

**Project No.:** 65  
**Programming Language:** Python 3  
**Project Type:** Menu-driven Console Application

## About the Project

The Hospital Management System is a simple Python console application for managing patient records. It allows a user to add, view, search, update, and delete patient information through a menu.

## Features

1. **Add Patient** – Add a patient record with a name, age, disease, and doctor's name.
2. **View All Patients** – Display all patient records.
3. **Search Patient** – Find a patient using their unique Patient ID.
4. **Update Patient** – Modify an existing patient's details.
5. **Delete Patient** – Remove a patient record using their Patient ID.
6. **Exit** – Close the application.

## Python Concepts Used

- Variables
- Dictionaries
- Functions
- `input()` and `print()`
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while` and `for`)
- String methods (`strip()` and `upper()`)
- Type conversion (`int()`)
- Exception handling (`try` and `except`)
- Dictionary methods (`get()` and `values()`)
- `return`, `break`, and `del`

## Requirements

- Python 3 installed on your computer
- Any code editor or IDE, such as Visual Studio Code, PyCharm, or IDLE

No external Python packages are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the Python file:

   ```bash
   python hospital_management_system.py
   ```

   On some systems, use:

   ```bash
   python3 hospital_management_system.py
   ```

4. Choose an option from the menu by entering a number from `1` to `6`.

## Menu

```text
========== HOSPITAL MANAGEMENT SYSTEM ==========
1. Add Patient
2. View All Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Exit
================================================
```

## How Patient Records Are Stored

Patient records are stored in a Python dictionary while the program is running. Each patient is identified by a unique ID, such as `P101`, `P102`, and so on.

A patient record contains:

- Patient ID
- Patient name
- Age
- Disease
- Doctor's name

## Important Note About Data Storage

This is a basic in-memory project. Patient records are stored temporarily in the program's memory. When the program is closed, the records are not saved permanently and will be lost. File or database storage is not included in this version.

## Learning Objective

This project demonstrates how basic Python concepts can be combined to build a menu-driven application and perform CRUD operations (Create, Read, Update, and Delete) on patient records.

## Author

Amit Kumbhakar

## License

This project is created for educational purposes.
