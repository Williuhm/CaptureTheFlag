import sys
import os
import re
import hashlib
import csv

# Check if a valid problem name and solution are provided as arguments
if len(sys.argv) != 3:
    print("Usage: submit <problem_name> <solution>")
    exit()

problem_name = sys.argv[1]
solution = sys.argv[2]

# Check if the provided problem number is valid
try:
    with open('/home/kali/Documents/sfaCS/Attempts/problems.csv', 'r') as prob_file:
        reader = csv.reader(prob_file)
        valid_problems = [row[0] for row in reader]

    if problem_name not in valid_problems:
        print("Not a valid problem number.")
        exit()

except FileNotFoundError:
    print("Problems file not found.")
    exit()

# Construct the file path based on the current user's login name
file_path = f"/home/kali/Documents/sfaCS/Attempts/attempts_{os.getlogin()}.csv"

# Check if the file exists and open it for reading
try:
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Read all rows into a list for manipulation
        for row in rows:
            # Extract the problem number, the corresponding hashed solution, and the solved status from each row
            stored_problem_name, stored_hashed_solution, solved = row
            # Check if the problem number from the file matches the provided problem number
            if stored_problem_name == problem_name:
                # Check if the problem has already been solved
                if hashlib.sha256(sys.argv[2].encode()).hexdigest() == stored_hashed_solution:
                    if solved == '1':
                        print("Problem has already been solved!")
                    else:
                        print("Problem solved!")
                        # Update the solved status to '1' in the CSV file
                        row[2] = '1'
                        with open(file_path, 'w', newline='') as update_file:
                            writer = csv.writer(update_file)
                            writer.writerows(rows)
                else:
                    print("Incorrect solution!")
                exit()
except FileNotFoundError:
    print("Attempts file not found.")

print("Problem not found in attempts file.")
