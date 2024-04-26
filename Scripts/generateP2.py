import os
import string
import random
import hashlib
import csv

# Problem number
prob = "problem2"
# Generate a random flag for the problem
flag = 'sfaCS{gr3p_1s_c00l_' + hashlib.sha256((str(os.getlogin()) + prob).encode()).hexdigest()[:8] + '}'
hashed_flag = hashlib.sha256(str(flag).encode()).hexdigest()  # Hash the flag

# Write the flag to the problem file
with open('problem2.txt', 'w') as f:
    f.write(''.join(random.choices(string.printable, k=random.randint(5000, 6000))))
    f.write('\n' + flag + '\n')
    f.write(''.join(random.choices(string.printable, k=random.randint(5000, 6000))))

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
        if row[0] == prob and row[1] == hashed_flag:
            flag_written = True
            break

# Write the flag to the attempts file if it hasn't been written
if not flag_written:
    with open(attempts_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([prob, hashed_flag, '0'])

print("New file problem2.txt created.")
print("Hint: Can I search for a word within a file?")
