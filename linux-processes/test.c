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
    
    printf("Salam from process with pid %d\n", getpid());
    return 0;
}