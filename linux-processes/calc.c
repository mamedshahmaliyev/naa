#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    printf("Length of inputs is: %d \n", argc);
    if (argc < 4) {
        printf("Invalid input! Example: calc 1 + 2 \n");
        return 1;
    }
    int result = 0;
    int a = atoi(argv[1]);
    int b = atoi(argv[3]);
    if (strcmp(argv[2], "+") == 0) {
        result = a + b;
    }
    else if (strcmp(argv[2], "-") == 0) {
        result = a - b;
    }
    else if (strcmp(argv[2], "-") == 0) {
        result = a - b;
    }
    else if (strcmp(argv[2], "*") == 0) {
        result = a * b;
    }
    else if (strcmp(argv[2], "/") == 0 && b != 0) {
        result = a / b;
    }

    printf("%s %s %s = %d \n", argv[1], argv[2], argv[3], result);
    return 0;
}
