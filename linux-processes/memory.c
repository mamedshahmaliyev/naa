#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif 

int main(int argc, char const *argv[])
{
    for (size_t i = 0; i < 5; i++)
    {
        char *ptr = malloc(500);
        printf("Got memory, address: %p\n", ptr);
    }
    return 0;
}
