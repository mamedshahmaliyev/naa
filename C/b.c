#include<stdio.h>
#include<stdlib.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
    char *programName = "sh";
    char *args[] = {programName, "b.sh", ".", NULL};
    execvp(programName, args);
}