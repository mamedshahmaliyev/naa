#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif 


int main(int argc, char* argv[]) {
    int parent_id = getpid();
    printf("Salam! Bu prosesin PID nomresi: %d \n", getpid());
    int fork_id = fork();
    // child process
    if (fork_id == 0) {
        printf("bala proses, id: %d \n", getpid());
        // sleep(3);
        printf("bala prosesin sonu! \n");
    }
    else if (fork_id > 0) {
        // b fayli yaradilana qeder gozle
        printf("ana proses, id: %d, yeni yaradilmish prosesin ID-i: %d \n", getpid(), fork_id);
        wait(NULL);
    }
    else {
        printf("Yeni bala proses yaradilmadi! \n");
    }
}