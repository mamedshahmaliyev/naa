#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

int fac(n) {
    if (n <= 1){
        return n;
    } 
    return n * fac(n-1);
}

int count = 0;

int mem[2000];
int fib(n) {
    if (n <= 1){
        return n;
    } 
    if (mem[n] > 0) 
        return mem[n];
    count++;
    mem[n] = fib(n-1) + fib(n-2);
    return mem[n];
}

int main(int argc, char const *argv[]){
    int n = 6;
    printf("%d\n", fib(n));
    printf("%d\n", count);
}
