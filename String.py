#Assignment 1: Create a string that contains a simple bio data like name, age, and country. Extract each piece of information and print them separately.
biodata = "Name: Faiza, Age: 24, Country: Bangladesh"

pairs = biodata.split(", ")

for pair in pairs:
    key, value = pair.split(": ")
    print(f"{key}: {value}")

# Assignment 2: Create a formatted string that includes data from a list or dictionary. For example, use a dictionary to store a person's information and format a string to include it.

person = {
    "name": "Faiza",
    "age": 24,
    "country": "Bangladesh",
}
formatted_string = (
    f"Name: {person['name']}\n"
    f"Age: {person['age']}\n"
    f"Country: {person['country']}"
    
)

print("Formatted String Using f-string:")
print(formatted_string)

# Assignment 3: Write a function that takes a string and returns a dictionary with the counts of each character in the string.
def count_characters(s):
    """
    Counts the occurrences of each character in the given string.

    Args:
        s (str): Input string.

    Returns:
        dict: Dictionary with characters as keys and their counts as values.
    """
    char_counts = {}
    
    for char in s:
        if char in char_counts:
            char_counts[char] += 1  # Increment count if character is already in dictionary
        else:
            char_counts[char] = 1  # Initialize count if character is not in dictionary
    
    return char_counts
input_string = "International Islamic University Chittagong"
result = count_characters(input_string)

print("Character Counts:")
for char, count in result.items():
    print(f"'{char}': {count}")