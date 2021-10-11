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
    int parent_pid = getpid();
    printf("Salam, press enter to execute... Process id is: %d\n", parent_pid);
    int fork_id = fork(); // fork() function return process id of child process and stores it in fork_id variable

    if (fork_id > 0) { // parent process

        printf("Parent process fork id is: %d\n", getpid());
        wait(NULL); // wait for all the children to finish
        printf("Bye \n");

    } else { // child process
        printf("Child process id is: %d\n", getpid());

        if (fork() > 0) { // child process
            printf("Process id is: %d\n", getpid());
            wait(NULL);
        } else { // child child proces
            printf("New Process id is: %d\n", getpid());
            sleep(5);
            printf("Child Child completed! \n");
        }
    }
}