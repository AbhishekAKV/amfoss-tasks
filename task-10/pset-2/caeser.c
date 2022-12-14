#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    if (argc != 2) {
        printf("Usage: ./file k\n");
        return 1;
    }

    int k = atoi(argv[1]);

    char s[999];
    printf("plaintext:  ");
    scanf("%[^\n]%*c", s);

    // Shift each character in the plaintext by k places
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = 'A' + (s[i] + k - 'A') % 26;
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = 'a' + (s[i] + k - 'a') % 26;
        }
    }

    printf("ciphertext: ");
    for (int i = 0; s[i] != '\0'; i++) {
        printf("%c", s[i]);
    }
    printf("\n");

    return 0;
}

