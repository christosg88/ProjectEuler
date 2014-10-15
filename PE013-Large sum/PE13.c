#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    FILE* fptr;
    if ((fptr = fopen("number.txt", "r")) == NULL)
    {
        printf("File not found. Exiting...\n");
        return 1;
    }

    int i, j, num, length, number[101][50];
    char buffer[50], c[2];

    for (j = 0; j < 50; ++j)
    {
        number[100][j] = 0;
    }

    for (i = 0; i < 100; ++i)
    {
        for (j = 0; j < 50; ++j)
        {
            fscanf(fptr, "%1d", &num);
            number[i][j] = num;
            number[100][j] += num;
        }
    }

    for (i = 49; i > 0; --i)
    {
        number[100][i-1] = number[100][i-1] + (number[100][i] / 10);
        number[100][i] = number[100][i] % 10;
    }

    sprintf(buffer, "%i", number[100][0]);

    length = strlen(buffer);

    if (length >= 10)
    {
        for (i = 0; i < 10; ++i)
        {
            printf("%c", buffer[i]);
        }
        printf("\n");
    }
    else
    {
        for (i = 1; i <= 10-length; ++i)
        {
            sprintf(c, "%i", number[100][i]);
            strcat(buffer, c);
        }

        for (i = 0; i < 10; ++i)
        {
            printf("%c", buffer[i]);
        }
        printf("\n");
    }

    return 0;
}