# Assignment 2: Use pip to install any library that is new to you and write a small script to explore its functionality.
import pyfiglet

def create_ascii_art(text, font="slant"):
    """
    Creates ASCII art text using pyfiglet.
    
    Args:
        text (str): The text to convert into ASCII art.
        font (str): The font style for the ASCII art. Default is "slant".
    
    Returns:
        str: ASCII art representation of the input text.
    """
    try:
        # Create ASCII art with the given text and font
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    # Input text and font
    text = "Hello, World!"
    font = "standard"  # Try "slant", "banner", "bubble", etc.

    # Generate and print ASCII art
    print(create_ascii_art(text, font))
