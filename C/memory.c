

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif 
#include <sys/stat.h>
#include <sys/mman.h>

void alloc_memory_examples() {

    // static
    int my_var = 99;

    int *dynamic_int = malloc(sizeof(int));
    int *arr = malloc(sizeof(int)*100);

    arr[90] = 21;
    arr[201] = 8; // may crash

    free(arr);
    arr = NULL;

    double *darr;
    darr = calloc(sizeof(double), 200);

    darr = realloc(darr, sizeof(double) * 500); // reallocate space, pointer could be changed from the original 
}

int main(int argc, char const *argv[])
{
    char s1[] = "NAA";

    printf("%s \n\n", s1);

    int i = 0;

    printf("%d\n", ++i);
    alloc_memory_examples();
    int *a = malloc(2);

    a[0] = 5;
    a[1] = 6;

    printf("%i\n", a[2]);

    int v = 8;

    int *shared_int = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);

    *shared_int = 8;

    int id = fork();

    if (id == 0) {
        printf("child pid = %d\n", getpid());
        v = 88;
        *shared_int = 88;
    } else {
        printf("parent pid = %d\n", getpid());
        wait(NULL);
    }

    printf("v = %i, pid = %d\n", v, getpid());
    printf("shared = %i, pid = %d\n", *shared_int, getpid());

    return 0;
}
