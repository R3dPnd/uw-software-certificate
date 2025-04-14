#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "common.h"

// gcc -o mem mem.c -Wall

/**
 * * This program allocates memory for an integer and then enters an infinite loop,
 * * The point of the class is to demonstrate that the memory is virtualized and not
 * * shared among running instances of the program.
 * * Each instance of the program will have its own copy of the integer and will not
 * * affect the other instances.
 */
int main(int argc, char *argv[])
{
    int *p = malloc(sizeof(int));
    assert(p != NULL);
    printf("(%d) address pointed to by p: %p\n",
           getpid(), p);
    *p = 0;
    while (1)
    {
        Spin(1);
        *p = *p + 1;
        printf("(%d) p: %d\n", getpid(), *p);
    }
    return 0;
}