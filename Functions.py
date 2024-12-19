# Assignment 1: Write a function that calculates the factorial of a number and handles any potential errors.
def calculate_factorial(n):
    """
    Calculates the factorial of a given number n.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the number.
    """
    try:
        # Ensure the input is a non-negative integer
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        
        # Base case for recursion
        if n == 0 or n == 1:
            return 1
        
        # Recursive calculation of factorial
        return n * calculate_factorial(n - 1)
    
    except ValueError as e:
        return f"Error: {e}"

num = -2

try:
    num = int(num)  # Try to convert the input to an integer
    result = calculate_factorial(num)
    print(f"The factorial of {num} is: {result}")
except ValueError:
    print("Error: Please enter a valid integer.")
