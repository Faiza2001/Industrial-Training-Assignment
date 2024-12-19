# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_file_path (str): Path to the input CSV file.
        json_file_path (str): Path to the output JSON file.
    """
    try:
        # Read the CSV file
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Convert each row into a dictionary and add it to a list
            data = [row for row in csv_reader]
        
        # Write the list of dictionaries to a JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"CSV file successfully converted to JSON and saved to {json_file_path}.")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_file_path = input("Enter the path to the CSV file: ")
json_file_path = input("Enter the path to save the JSON file: ")

csv_to_json(csv_file_path, json_file_path)

# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.
from datetime import datetime

def write_log(message, log_file_path):
    """
    Appends a log message with a timestamp to a log file.

    Args:
        message (str): The log message to write.
        log_file_path (str): Path to the log file.
    """
    try:
        with open(log_file_path, mode='a', encoding='utf-8') as log_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"[{timestamp}] {message}\n")
        print("Log message written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

write_log("Application started", 'data/logs.txt')
write_log("Error: Failed to connect to the database", 'data/logs.txt')
write_log("Application terminated", 'data/logs.txt')
