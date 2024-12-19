# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.
# Initial student dictionary
student = {
    "name": "Faiza",
    "roll_number": 201213,
    "grades": [
        {"subject": "Graphics", "marks": 90},
        {"subject": "English", "marks": 85},
        {"subject": "Network", "marks": 88}
    ]
}

# Initial dictionary
print("Initial Student Dictionary:")
print(student)

# Adding a new subject
student["grades"].append({"subject": "Security", "marks": 80})
print(student)

# Modifying marks for Graphics
for grade in student["grades"]:
    if grade["subject"] == "Graphics":
        grade["marks"] = 95
print(student)

# Removing the subject English
student["grades"] = [grade for grade in student["grades"] if grade["subject"] != "English"]
print(student)

# Updating the student's name
student["name"] = "Faiza Ali"
print(student)

#Assignment-2:Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student. 

students = {
    "Falaq": [85, 90, 88],
    "Fatiha": [78, 82, 84],
    "Mihirimah": [92, 95, 94],
    "Tanjila": [88, 85, 91]
}

print("Average Grades:")
for name, grades in students.items():
    average = sum(grades) / len(grades)  # Calculate average
    print(f"{name}: {average:.3f}")

# Assignments 4: Write a regex to find the Bangladesh phone number with all variations.
import re

phone_numbers = [
    "01454565767",
    "+880196345634",
    "0088785674657",
    "01845-567567",
    "123456789",  
    "+8802-3456"  
]

# Regex to match all Bangladesh phone number variations
pattern = r"(?:\+880|0088|01[3-9])\d{1}-?\d{3,5}-?\d{3,5}"

valid_numbers = [num for num in phone_numbers if re.fullmatch(pattern, num)]

print("Valid Bangladesh Phone Numbers:")
print(valid_numbers)
