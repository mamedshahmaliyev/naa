#include <signal.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif 
#include <stdio.h>

int main(int argc, char const *argv[])
{
    printf("Salam from main process with pid %d\n", getpid());
    getchar();
    return 0;
}
