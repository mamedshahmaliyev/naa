
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>


/**
 * parallelism vs concurency
 * threads vs processes
 * joins
 * mutex lock
 * mutex deadlock
 * thread params and return values
 * windows support of pthreads
 */

void* green(void* a) 
{
    while (1)
    {
        printf("green\n");
        sleep(1);
    }
    return NULL;
}

void* yellow(void* a) 
{
    while (1)
    {
        printf("yellow\n");
        sleep(1);
    }
    return NULL;
}

void* red(void* a) 
{
    while (1)
    {
        printf("red\n");
        sleep(1);
    }
    return NULL;
}
void* prnt(void* a) 
{
    int * v = (int *)a;
    int * c = (int *) malloc(sizeof(int));
    while (*v > 0)
    {
        printf("%d\n", *v);
        *v = *v - 1;
        *c = *c + 1;
        sleep(1);
    }
    return c;
}


// basic demo
int main_basic(int argc, char const *argv[])
{
    pthread_t thread_green;
    pthread_t thread_yellow;
    pthread_t thread_red;
    pthread_t thread_prnt;
    
    pthread_create(&thread_green, NULL, green, NULL);
    pthread_create(&thread_yellow, NULL, yellow, NULL);
    pthread_create(&thread_red, NULL, red, NULL);

    int v = 4;
    pthread_create(&thread_prnt, NULL, prnt, &v);

    void * vr;
    pthread_join(thread_prnt, &vr); // wait for thread to finish its job

    printf("%d \n", *(int *) vr);
    
    return 0;
}



int cnt = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void* simple_counter( void * a) 
{
    for (int i = 0; i < 1000000000; i++)
    {
        pthread_mutex_lock(&lock);
        cnt++;
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

// lock demo
int main(int argc, char const *argv[])
{

    pthread_t th;

    pthread_create(&th, NULL, simple_counter, NULL);
    simple_counter(NULL);

    pthread_join(th, NULL);
    
    printf("%d \n", cnt);
    return 0;
}


