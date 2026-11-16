"""
Hospital Management System
Project No.: 65
Language: Python 3

A menu-driven console application to manage patient records.
Data is stored in memory while the program is running (no file/database).
"""

patients = {}
next_patient_number = 101


def add_patient():
    """Add a new patient after validating the required details."""
    global next_patient_number

    print("\n--- Add New Patient ---")
    name = input("Enter patient name: ").strip()

    if not name:
        print("Invalid name. Name cannot be empty.")
        print("Patient not added.")
        return

    age_text = input("Enter patient age (0-120): ").strip()

    try:
        age = int(age_text)
        if age < 0 or age > 120:
            raise ValueError
    except ValueError:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not added.")
        return

    disease = input("Enter disease: ").strip()
    doctor = input("Enter doctor's name: ").strip()

    if not disease or not doctor:
        print("Disease and doctor's name cannot be empty.")
        print("Patient not added.")
        return

    patient_id = f"P{next_patient_number}"
    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "disease": disease,
        "doctor": doctor
    }

    patients[patient_id] = patient
    next_patient_number += 1

    print(
        f"Patient added. ID: {patient_id} | {name} | "
        f"{age} | {disease} | {doctor}"
    )


def view_patients():
    """Display all patient records."""
    print("\n--- All Patient Records ---")

    if not patients:
        print("No patient records found.")
        return

    for patient in patients.values():
        print(
            f"ID: {patient['id']} | Name: {patient['name']} | "
            f"Age: {patient['age']} | Disease: {patient['disease']} | "
            f"Doctor: {patient['doctor']}"
        )


def search_patient():
    """Search for a patient using the patient ID."""
    print("\n--- Search Patient ---")
    patient_id = input("Enter patient ID (e.g. P101): ").strip().upper()

    patient = patients.get(patient_id)
    if patient is None:
        print("Patient ID not found.")
        return

    print(
        f"ID: {patient['id']} | Name: {patient['name']} | "
        f"Age: {patient['age']} | Disease: {patient['disease']} | "
        f"Doctor: {patient['doctor']}"
    )


def update_patient():
    """Update the disease and/or other details of an existing patient."""
    print("\n--- Update Patient ---")
    patient_id = input("Enter patient ID to update: ").strip().upper()

    patient = patients.get(patient_id)
    if patient is None:
        print("Patient ID not found.")
        return

    print("Press Enter to keep the current value.")

    new_name = input(f"Name [{patient['name']}]: ").strip()
    if new_name:
        patient["name"] = new_name

    new_age_text = input(f"Age [{patient['age']}]: ").strip()
    if new_age_text:
        try:
            new_age = int(new_age_text)
            if not 0 <= new_age <= 120:
                raise ValueError
            patient["age"] = new_age
        except ValueError:
            print("Invalid age. Age must be a number between 0 and 120.")
            print("Age was not changed; other valid changes will be saved.")

    new_disease = input(f"Disease [{patient['disease']}]: ").strip()
    if new_disease:
        patient["disease"] = new_disease

    new_doctor = input(f"Doctor [{patient['doctor']}]: ").strip()
    if new_doctor:
        patient["doctor"] = new_doctor

    print(
        f"Patient {patient_id} updated. Disease: {patient['disease']}"
    )


def delete_patient():
    """Delete a patient record using the patient ID."""
    print("\n--- Delete Patient ---")
    patient_id = input("Enter patient ID to delete: ").strip().upper()

    if patient_id not in patients:
        print("Patient ID not found.")
        return

    del patients[patient_id]
    print(f"Patient {patient_id} deleted. Total patients: {len(patients)}")


def display_menu():
    """Display the main menu."""
    print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")
    print("================================================")


def main():
    """Run the application until the user chooses Exit."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            print("Thank you for using the Hospital Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
