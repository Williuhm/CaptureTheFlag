# Take encrypted_flag as input from the user
encrypted_flag = input()

# Decrypt the flag
flag = list(encrypted_flag)
for i in range(0, len(encrypted_flag), 3):
    flag[i], flag[i + 1], flag[i + 2] = flag[i + 1], flag[i + 2], flag[i]

decrypted_flag = ''.join(flag)

print("Decrypted flag:", decrypted_flag)





