import os
import csv
import hashlib
import random

# Problem number
prob = "problem5"
# Generate a random flag for the problem
flag = 'sfaCS{th3_numb3r5_m450n_' + hashlib.sha256((str(os.getlogin()) + prob).encode()).hexdigest()[:8] + '}'
hashed_flag = hashlib.sha256(str(flag).encode()).hexdigest()  # Hash the flag

random_seed = int(hashlib.sha256((str(os.getlogin()) + prob).encode()).hexdigest()[:8], 16)
random.seed(random_seed)

char_set = 'abcdefghijklmnopqrstuvwxyz0123456789_'
new_flag = ''

for c in flag[6:-1]:
	num = (random.randint(1,12) * 37) + char_set.index(c)
	new_flag = new_flag + str(num) + ' '
	
flag = new_flag

# Write the flag to the problem file
with open('problem5.txt', 'w') as f:
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

print("New file problem5.txt created.")
print("Hint: I made a new encryption! Each number's remainder after")
print("dividing by 37 corresponds to a character. 0-25 are a-z, 26-35")
print("are 0-9, and 36 is an underscrore! Submit the flag as")
print("sfaCS{decrypted_flag}")
