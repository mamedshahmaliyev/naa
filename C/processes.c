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

    printf("Salam from main process with pid %d\n", getpid());
    int fork_id = fork();

    // child process
    if (fork_id == 0) {
        printf("Inside the child process with pid %d (fork id is: %d) \n", getpid(), fork_id);
        printf("Sleep for 2 seconds... \n");
        sleep(2);

        printf("Executing ls program inside child process \n");
        char *programName = "ls";
        char *args[] = {programName, "-lha", ".", NULL};
        execvp(programName, args);
    }
    else if (fork_id > 0) {
        printf("Inside the parent process with pid %d (fork id is: %d) \n", getpid(), fork_id);
        printf("Waiting for child to finish...\n");
        int wc = wait(NULL);
        printf("Child processes terminated!\n");
        printf("Press enter to exit...");
        getchar();
    }
    return 0;
}