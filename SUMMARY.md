# PROJECT SUMMARY

## Project Title
**Hospital Management System**

## Project Number
**Project No. 65**

## Programming Language
Python 3

## Project Description
The Hospital Management System is a simple, menu-driven Python console application. It helps manage basic patient information. The user can add new patient details, view all patient records, search for a patient, update patient information, and delete a patient record.

## Main Features
1. **Add Patient** – Adds a new patient's details and assigns a unique patient ID.
2. **View All Patients** – Displays the details of all patients stored in the program.
3. **Search Patient** – Finds a patient using the patient ID.
4. **Update Patient** – Changes the saved details of an existing patient.
5. **Delete Patient** – Removes a patient record using the patient ID.
6. **Display Menu** – Shows the available operations.
7. **Main Function** – Runs the menu repeatedly until the user chooses to exit.

## Python Concepts Used
- Variables and data types
- `input()` and `print()`
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`)
- Functions
- Dictionary
- Exception handling (`try` and `except`)
- Dictionary methods such as `.get()` and `.values()`

## How the Project Works
When the program starts, it displays a menu. The user selects an option by entering its number. The program then performs the selected operation. The menu appears again after the operation, until the user chooses the exit option.

## Data Storage
Patient records are stored in a Python dictionary while the program is running. **The current version does not use a database or save records permanently.** The records are lost when the program is closed.

## How to Run
1. Install Python 3.
2. Keep `hospital_management_system.py` in the project folder.
3. Open a terminal or command prompt in that folder.
4. Run:

```bash
python hospital_management_system.py
```

## Conclusion
This project demonstrates the basic use of Python programming concepts to create a simple patient-record management application. It provides practice with functions, loops, conditions, dictionaries, and basic data operations.

