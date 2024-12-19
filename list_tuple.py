#Assignment-1:Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.
matrix = [
    [5, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Accessing element
print(matrix[0][0])  
print(matrix[1][2])  
print(matrix[2][0])  
#modifying element
matrix[0][0] = 1
matrix[2][2] = 10
print(matrix)
#iterating through each element
for row in matrix:
    for element in row:
        print(element, end=" ")
print()

#Assignment-2:Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
# Tuple with mixed data types
mixed_tuple = (111, "Faiza", True, 10)

print("Tuple with mixed data types:", mixed_tuple)

# Dictionary with tuples as values
user_data = {
    1: ("Alice", 25, "Engineer"),  # (Name, Age, Profession)
    2: ("Bob", 30, "Designer"),
    3: ("Charlie", 28, "Doctor")
}

# Accessing data
print("\nUser 1's data:", user_data[1])
print("Name of User 1:", user_data[1][0])

# List of tuples
employee_list = [
    (1, "Alice", "Engineer"),
    (2, "Bob", "Designer"),
    (3, "Charlie", "Doctor")
]
print("\nEmployee List:")
for emp in employee_list:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Profession: {emp[2]}")
print()

# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.
students = [
    ("Falaq", 99),
    ("Fatiha", 92),
    ("Mihirimah", 88),
    ("Faiza", 95),
    ("Tanjila", 98)
]

sorted_students = sorted(students, key=lambda x: x[1])

print("Students sorted by grades (ascending):")
for student in sorted_students:
    print(f"{student[0]}: {student[1]}")

