
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

void * fibonacchi_t(void * a)
{
    int* n1 = malloc(sizeof(int));
    int* n2 = malloc(sizeof(int));
    long* Fn = malloc(sizeof(long));

    int n = *(int *)a;
    if (n <= 2) {
        *Fn = 1;
        return Fn;
    }
    
    *n2 = n - 2;
    *n1 = n - 1;

    // long a2 = *(long *) fibonacchi_t(n2);

    pthread_t th2;
    pthread_create(&th2, NULL, fibonacchi_t, n2);
    void * a2;

    pthread_t th1;
    pthread_create(&th1, NULL, fibonacchi_t, n1);
    void * a1;

    
    pthread_join(th2, &a2);
    pthread_join(th1, &a1);

    *Fn = (*(long *)a2) + (*(long *)a1);
    return Fn;
}


long fibonacchi(int n)
{
    if (n <= 2) return 1;
    long a2 = fibonacchi(n - 2);
    long a1 = fibonacchi(n - 1);
    return a1 + a2;
}

int main(int argc, char const *argv[])
{
    int n = atoi(argv[1]);
    // printf("Fibonacci sequence calculator, F(%d) = %ld\n", n, fibonacchi(n));
    printf("Fibonacci sequence calculator, F(%d) = %ld\n", n, *(long*)fibonacchi_t(&n));
}


