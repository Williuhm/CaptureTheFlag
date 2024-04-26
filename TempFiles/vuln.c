#include <stdio.h>
#include <string.h>

char flag[] = "REDACTED";

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
