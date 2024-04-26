import os
import csv
import hashlib

# Problem number
prob = "problem1"
# Generate a random flag for the problem
flag = 'sfaCS{ju5t_g3tt1ng_5t4rt3d_' + hashlib.sha256((str(os.getlogin()) + prob).encode()).hexdigest()[:8] + '}'
hashed_flag = hashlib.sha256(str(flag).encode()).hexdigest()  # Hash the flag

# Write the flag to the problem file
with open('problem1.txt', 'w') as f:
    f.write('' + flag + '')

# Check if the attempts file exists, create it if it doesn't
attempts_file_path = '/home/kali/Documents/sfaCS/Attempts/attempts_' + str(os.getlogin()) + '.csv'
if not os.path.isfile(attempts_file_path):
    with open(attempts_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['problem_name', 'hashed_solution', 'solved'])

# Check if the flag has already been written to the attempts file
flag_written = False
with open(attempts_file_path, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == prob and row[1] == hashed_flag:  # Compare with the hashed flag
            flag_written = True
            break

# Write the flag to the attempts file if it hasn't been written
if not flag_written:
    with open(attempts_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([prob, hashed_flag, '0'])  # Assuming '0' indicates not solved

print("New file problem1.txt created.")
print("Hint: A new file? How can I read the contents?")
