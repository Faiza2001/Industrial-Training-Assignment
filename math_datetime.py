# Assignment 1: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).
def calculate_compound_interest(P, r, n, t):
    """
    Calculates compound interest.

    Args:
        P (float): Principal amount.
        r (float): Annual interest rate (as a decimal, e.g., 0.05 for 5%).
        n (int): Number of times interest is compounded per year.
        t (float): Time in years.

    Returns:
        float: Total amount after interest.
    """
    try:
        # Validate inputs
        if P < 0 or r < 0 or n <= 0 or t < 0:
            raise ValueError("Inputs must be non-negative, and n must be greater than zero.")
        
        # Calculate compound interest
        A = P * (1 + r / n) ** (n * t)
        return round(A, 2)
    except Exception as e:
        return f"Error: {e}"

# Example Usage
principal = 1000  # Principal amount in dollars
rate = 0.05       # Annual interest rate (5%)
compounds_per_year = 4  # Quarterly compounding
time_in_years = 10  # Duration in years

amount = calculate_compound_interest(principal, rate, compounds_per_year, time_in_years)
print(f"The total amount after interest is: ${amount}")

# Assignment 2: Create a script that prints the current time and updates every second.
import time

def live_clock():
    """
    Prints the current time and updates every second.
    """
    try:
        while True:
            # Get the current time
            current_time = time.strftime('%H:%M:%S', time.localtime())
            
            # Print the current time, overwriting the previous output
            print(f"\rCurrent Time: {current_time}", end="")
            
            # Wait for 1 second
            time.sleep(1)
    except KeyboardInterrupt:
        # Gracefully handle the exit when user presses Ctrl+C
        print("\nClock stopped.")

# Run the live clock
live_clock()
