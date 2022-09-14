#include <stdio.h>

#include "exec.h"

void outprint(char const *argv)
{
    char buffer[80];
    FILE *fp = popen(argv, "r");
    fgets(buffer, sizeof(buffer), fp);
    printf("%s\n", buffer);
    pclose(fp);
}
