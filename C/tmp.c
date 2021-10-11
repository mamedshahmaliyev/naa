#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

// print red to the output every second
void * print_number(void * arg) {
    int* n = (int *) arg;
    while(1 == 1) {
        printf("%d \n", *n);
        sleep(1);
    }
}

void * square(void * arg) {
    int a = *(int *) arg;

    int * area = malloc(sizeof(int));

    *area = a * a;

    return area;
}

int main(int argc, char const *argv[])
{
    int a = 5;
    pthread_t t;
    pthread_create(&t, NULL, square, &a);

    void * area;
    pthread_join(t, &area);
    printf("area is %d \n", *(int *) area);
}
