# Character set
char_set = 'abcdefghijklmnopqrstuvwxyz0123456789_'

# Take encrypted_flag as input from the user
encrypted_flag = input()

# Decrypt the flag
decrypted_flag = ''
for num_str in encrypted_flag.split():
    num = int(num_str)
    decrypted_flag += char_set[num % 37]

print("Decrypted flag:", decrypted_flag)
