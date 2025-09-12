import json  # For reading/writing JSON files
import os    # For checking if the file exists

FILE_NAME = "tasks.json"  # Name of the file where tasks are stored

def load_tasks():
    # Loads tasks from the JSON file if it exists
    if not os.path.exists(FILE_NAME):
        return []  # Return empty list if file doesn't exist
    with open(FILE_NAME, "r") as file:
        return json.load(file)  # Return list of task dictionaries

def save_tasks(tasks):
    # Saves the list of task dictionaries to the JSON file
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)  # Pretty-print with indentation