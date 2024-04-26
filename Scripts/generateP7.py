import os
import csv
import hashlib
import subprocess

# Problem number
prob = "problem7"
# Generate a random flag for the problem
flag = 'sfaCS{buff3r_0v3rfl0w_' + hashlib.sha256((str(os.getlogin()) + prob).encode()).hexdigest()[:8] + '}'
hashed_flag = hashlib.sha256(str(flag).encode()).hexdigest()  # Hash the flag

# Write the flag to the problem file
with open('problem7.c', 'w') as f:
    f.write(
    f"""
#include <stdio.h>
#include <string.h>

char flag[] = "{flag}";

    """
    )
    f.write(
    """

void checkPass() {
    char buffer[32];
    printf("Enter the password: ");
    gets(buffer);

    if (strcmp(buffer, flag) == 0) {
        printf("Password is correct! Submit your flag!\\n");
    } else {
        printf("Incorrect password.\\n");
    }
}

void hidden() {
    printf("%s\\n", flag);
}

int main() {
    checkPass();
    return 0;
}
    """
    )
    
try:
    subprocess.run(["gcc", "-O0", "-fno-builtin", "-fno-stack-protector", "-m32", "-std=c11", "-ggdb", "-z", "execstack", "-o", "problem7", "problem7.c"], stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError as e:
    print("Compilation failed:", e)
    
os.remove("problem7.c")
    
with open('problem7.c', 'w') as f:
    f.write(
    """
#include <stdio.h>
#include <string.h>

char flag[] = "[REDACTED]";

void checkPass() {
    char buffer[32];
    printf("Enter the password: ");
    gets(buffer);

    if (strcmp(buffer, flag) == 0) {
        printf("Password is correct! Submit your flag!\n");
    } else {
        printf("Incorrect password.\n");
    }
}

void hidden() {
    printf("%s\n", flag);
}

int main() {
    checkPass();
    return 0;
}
    """
    )
    
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

print("New files problem7.c and problem7 created.")
print("Hint: The source code from problem7 can be found in problem7.c")
print("Use the source code to retrieve the hidden flag from the")
print("compiled code.")
