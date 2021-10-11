#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif 

int main(int argc, char* argv[]) {

    // static
    int my_var = 99;

    int *dynamic_int = malloc(sizeof(int));
    int *arr = malloc(sizeof(int)*100);

    printf("%d\n", dynamic_int);

    // arr[90] = 21;
    // arr[201] = 8; // may crash

    // free(arr);
    // arr = NULL;

    return 0;
}