import os
import csv
import hashlib
import subprocess

subprocess.run(['bash', '/home/kali/Documents/sfaCS/Scripts/alias.sh'])
# Problem number
prob = "problem0"
# Generate a random flag for the problem
flag = 'sfaCS{h0us3_rul3s_' + hashlib.sha256((str(os.getlogin()) + prob).encode()).hexdigest()[:8] + '}'

# Write the flag to the problem file
with open('README.txt', 'w') as f:
    f.write(
    f"""
Welcome to the Rules and Information for the Stephen F. Austin State
University Computer Science Capture The Flag Project

Type 'q' to exit.

# Introduction

## What is a Computer Science Capture The Flag?

A computer science capture the flag is a game targetted at aspiring
programmers. The game includes multiple intentionally vulnerable
products for users to hack, decrypt, break, or gain access to using
whatever it takes to find the flag.

## What is "the flag"?

The flag is a string of text hidden within each challenge that will
follow a pattern. Every flag starts with the text "sfaCS{{" and ends
with "}}". Between the braces, there are characters that will make a
phrase or some random values. Speaking of flags, you just found
your first flag for problem0: {flag}

## What to do with the flag?

Once you have the flag, use the python script called 'submit' in
the parent folder with the problem name and the problem's flag.
This command can be found below for a better idea on the usage of
the script.

# Rules

- No cheating. Sharing answers is not allowed and will be noted.

- Don't break the server. Others use it and we can find out who
  caused the issue. We will revoke your access to the problems.
  
- This project is still in development. If there are bugs, errors,
  or any other issues. Report them and don't abuse them. I will
  fix it to the best of my ability. 
  
# Commands

This is a list of important commands and what they do. Refer back
to this list if you get stuck, lost, or forget anything.

- Use 'ls' to list the files in the current directory.

- Use 'cd <PATH>' to change the current directory. Use 'cd ..' to
  go up one folder to the parent folder.
  
- Use 'cat <FILE>' to print the contents of a file to the screen.

- Use (CTRL) + (C) to terminate a process if it's running too long.

- Use 'man <COMMAND>' for more information about a command.

- Use 'logout' to close the terminal and leave your session.

- Use 'python3 ../generateP#.py' to generate a problem with that
  number. Replace the # with the problem you would like to attempt.
  
- Use 'python3 ../submit.py problem# <FLAG>' to submit an attempt
  for a problem. Replace the # with the problem you would like to
  attempt.
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
        if row[0] == prob and row[1] == hashlib.sha256(str(flag).encode()).hexdigest():
            flag_written = True
            break

# Write the flag to the attempts file if it hasn't been written
if not flag_written:
    with open(attempts_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([prob, hashlib.sha256(str(flag).encode()).hexdigest(), '0'])

print("================================================================")
print("Welcome to the Stephen F. Austin State University Computer")
print("Science Capture The Flag Project")
print()
print("For rules and information, type\033[95m less README.txt\033[0m")
print("================================================================")
