#include <stdio.h> // preprocessor directive
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <string.h>

// numbers, arrays, structs and pointers
// operators ++y vs y++, %, =, ==, !=
// bitwise <<, >>, &, |, ^, ~

struct Person {
    char name[50];
    int age;
};

int str_length(char * s) {
    int i = 0;
    while (s[i] != 0) {
        i++;
    }
    return i;
}
// every string is array of chars ending with null terminating character 0 
void strings() {
    // \t, \n, escape character
    char *s1 = "Salam"; // 6 bytes because of terminator character [S,a,l,a,m,0]
    char s2[] = "Salam";
}

void reverse0(char * s) {
    int length = strlen(s);
    for (int i = 0; i < length/2; i++)
    {
        char tmp = s[i];
        s[i] = s[length - i - 1];
        s[length - i - 1] = tmp;
    }
}
char * reverse2(char * s) {
    int length = strlen(s);
    char *res = malloc(length + 1); // +1 if for terminator
    for (int i = 0; i < length; i++)
    {
        res[i] = s[length - i - 1];
    }
    res[length] = 0;
    return res;
}

// function definition
int main(int argc, char const *argv[])
{
    int y = 7;
    int *p = &y; // store address of variable y
    printf("%p, %i\n", p, *p);
    *p = 14;
    printf("%p, %i\n", p, *p);

    int x[2];
    x[0] = 1;
    x[1] = 2;

    int8_t a = 2;

    printf("%i, %i\n", x[0], x[1]);

    struct Person mamed;
    mamed.age = 22;

    printf("%i\n", mamed.age);

    int arr[3] = {1,2,3};

    int8_t *p1 = arr;

    printf("%p, %p, %p\n", p1, p1 + 1, p1 + 2);


    srand(time(0));
    int random_number = rand();
    printf("Salam, the random number is: %i\n", random_number);

    printf("%s\n", reverse2("salam"));
    return 0;
}
