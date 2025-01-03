import csv
from datetime import datetime

logged_names = set()

def initialize_csv(file_path):
    """
    Create a new CSV file with a header.
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Timestamp'])

def record_attendance(name, file_path):
    """
    Record attendance for the detected name.
    """
    if name not in logged_names:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, datetime.now()])
        logged_names.add(name)
        print(f"Attendance recorded for: {name}")
