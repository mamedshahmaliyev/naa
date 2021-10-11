#include<stdio.h>
#include<stdlib.h>

// pointers

int main(int argc, char const *argv[])
{
    char *a = "NAA"; // [N,A,A,0]
    char *c = malloc(2);
    c[0] = a[1];

    printf("%s", c);
    
    return 0;
}


// int main(int argc, char const *argv[])
// { 
//     int32_t a[] = {1, 2, 3, 4};

//     int32_t *p = a;

//     printf("%p, %p, %p, %p", p, p + 1, p + 2, p+3);
//     printf("\n");
// }
