#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>

int child_process_finished = 0;

void handler(int signal_code) {
    printf("Signal (code: %d) handler is overriden, i won't die! )", signal_code);
}
void sigusr1_handler(int signal_code) {
    child_process_finished = 1;
}

int main(int argc, char const *argv[])
{
    int parent_pid = getpid();
    signal(SIGINT, handler); // CTRL+C
    signal(SIGTERM, handler); // KILL pid or kill -TERM pid
    // signal(SIGKILL, handler); // this will not work, kill -9 pid

    int fork_pid = fork();

    if (fork_pid == 0) {
        printf("Inside child process (bala proses) pid: %d\n", getpid());
        printf("1...........\n");
        printf("Press Enter to continue (Davam etmək üçün Enteri sıxın)....\n");
        getchar();
        printf("2...........\n");
        kill(parent_pid, SIGUSR1);
    } else if (fork_pid > 0) {
        signal(SIGUSR1, sigusr1_handler);
        printf("Inside parent process (ana proses) pid: %d\n", getpid());
        while (child_process_finished != 1) {
            printf("Waiting for child process to finish (Bala prosesin bitməsini gözləyir) [%d, %d]...\n", parent_pid, fork_pid);
            sleep(2);
        }
        printf("Print this after child process is finished (bu sətir bala proses bitdikdən sonra çap olunur)...\n");
        printf("3..........\n");
    } else {
        printf("Fork error...\n");
    }
    // while(1) {
    //     printf("Running forever (pid: %d)...\n", getpid());
    //     sleep(1);
    // }
    return 0;
}
