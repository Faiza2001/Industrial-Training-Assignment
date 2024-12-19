# Assignment 1: Write a Python script that determines if a number is positive, negative, or zero using if-elif-else.

number = 90

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Assignment 2: Create a script that checks if a person is eligible for a senior citizen discount based on age and residency.
# Input: Get the person's age and residency status
age = int(input("Enter your age: "))
is_resident = input("Are you a resident of the city? (yes/no): ").strip().lower()

if (age >= 65) or (is_resident == "yes" and age >= 60):
    print("You are eligible for the senior citizen discount.")
else:
    print("You are not eligible for the senior citizen discount.")

# Assignment 3: Write a script that simulates a basic login system. Check username and password correctness.

correct_username = "admin"
correct_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")

# Assignment 4: Implement a system that categorizes a day based on temperature and weather conditions.
# Use nested if-elif-else and logical operators to determine if it's a beach day, skiing day, or a stay-home day.

temperature = float(input("Enter the temperature (in Celsius): "))
weather = input("Enter the weather condition (sunny, snowy, rainy, cloudy): ").strip().lower()

# Determine the type of day based on temperature and weather
if temperature >= 30 and weather == "sunny":
    print("It's a beach day!")
elif temperature <= 0 and weather == "snowy":
    print("It's a skiing day!")
else:
    if weather == "rainy" or weather == "cloudy":
        print("It's a stay-home day due to bad weather.")
    elif 10 <= temperature < 30:
        print("It's a stay-home day, maybe a good day for indoor activities.")
    else:
        print("It's a stay-home day, too extreme for outdoor activities.")

