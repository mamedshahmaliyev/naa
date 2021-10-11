#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif 
#include <sys/mman.h>

int main(int argc, char* argv[]) {

    
    // long s = 0;
    // for (long i = 0; i < 9000000000; i++) {
    //     s += i;
    // }
    // printf("Sum: %ld\n", s);

    long *s = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    *s = 0; // use asterisk to change the value of the pointer
    
    if (fork() > 0) {
        for (long i = 0; i < 4000000000; i++) {
            *s += i;
        }
        wait(NULL);
        printf("Sum: %ld\n", s);
    } else {
        for (long j = 4000000000; j < 9000000000; j++) {
            *s += j;
        };
    }
}