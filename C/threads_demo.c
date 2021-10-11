
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

void * job_one_sec(void * job_num)
{
    sleep(1);
    printf("DONE: %d\n", *(int*) job_num);
    return NULL;
}




int main(int argc, char const *argv[])
{
    int n = atoi(argv[1]);
    srand(time(NULL));

    pthread_t t[n];
    
    for (int j = 0; j < n; j++)
    {
        if (1 == 1) {
            pthread_t th1;
            int* job_num = malloc(sizeof(int)*5);
            *job_num = j;
            pthread_create(&t[j], NULL, job_one_sec, job_num);
        } else {
            job_one_sec(&j);
        }
        
    }
    for (int j = 0; j < n; j++)
    {
        if (t[j]) pthread_join(t[j], NULL);
    }
}


