
#include<stdio.h>

void printElementsOfArrWithoutLoop(int arr[]) {
    printf("Printing the elements of array without loop:\n");
    printf("1st element: %i\n", arr[0]);
    printf("2nd element: %i\n", arr[1]);
    printf("3rd element: %i\n", arr[2]);
    printf("4th element: %i\n", arr[3]);
}
void printElementsOfArrWithForLoop(int arr[], int size) {
    printf("Printing the elements of array with for loop:\n");
    for (int i = 0; i < size; i++)
    {
        printf("The element %i of arr is: %i\n", i + 1, arr[i]);
    }
}
void printElementsOfArrWithWhileLoop(int arr[], int size) {
    printf("Printing the elements of array with while loop:\n");
    int i = 0;
    while (i < size) {
        printf("The element %i of arr is: %i\n", i + 1, arr[i]);
        i++;
    }
}
void printElementsOfArrWithDoWhileLoop(int arr[], int size) {
    printf("Printing the elements of array with do while loop:\n");
    int i = 0;
    do {
        printf("The element %i of arr is: %i\n", i + 1, arr[i]);
        i++;
    } while (i < size);
}


void reverseArrUsingSecondArr() {
    int arr[] = {1, 2, 3, 4, 5};
    int arr2[] = {0, 0, 0, 0, 0};
    int i = 0;
    while (i <= 4) {
        arr2[i] = arr[4 - i];
        i++;
    }
    printf("first arr: ");
    for (int i=0; i < 5; i++) printf("%i ", arr[i]);
    printf("\nreversed arr: ");
    for (int i=0; i < 5; i++) printf("%i ", arr2[i]);
    printf("\n");
}

int main(int argc, char const *argv[])
{
    // int arr[] = {1, 2, 3, 4};
    
    // printElementsOfArrWithoutLoop(arr);
    // printElementsOfArrWithForLoop(arr, 4);
    // printElementsOfArrWithWhileLoop(arr, 4);
    // printElementsOfArrWithDoWhileLoop(arr, 4);

    // int a = 5;
    // // first check for condition, then execute
    // while (a < 5) {
    //     printf("inside while loop, the value of a is %i\n", a);
    //     a++;
    // }

    // int b = 5;
    // // first execute, then check condition
    // do {
    //     printf("inside while loop, the value of a is %i\n", b);
    //     b++;
    // }  while (b < 5);
    // printf("inside while loop, the value of a is %i\n", b);


    int arr[] = {1, 2, 3, 4, 5};
    int i = 0;
    while (i <= 1) {
        int tmp = arr[i];
        arr[i] = arr[4 - i];
        arr[4 - i] = tmp;
        i++;
    }
    printf("Reversed arr: ");
    for (int i = 0; i < 5; i++) printf("%i ", arr[i]);
    printf("\n");
    



    return 0;
}
