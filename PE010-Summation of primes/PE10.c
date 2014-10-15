#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./pe10 end\n");
        return 1;
    }

    unsigned long long int i, j, num, sum = 0, end = atoi(argv[1]);
    bool flag, is_prime;
    FILE* fptr;
    if ((fptr = fopen("primes.txt", "r+")) == NULL)
    {
        printf("Creating new file.\n");
        if ((fptr = fopen("primes.txt", "w+")) == NULL)
        {
            printf("Error creating the file.\n");
            return 2;
        }
        else
        {
            num = 2;
            fprintf(fptr, "%llu\n", num);
        }
        
    }
    else
    {
        printf("File exists.\n");
    }

    while ((fscanf(fptr, "%llu", &num) != EOF) && num <= end)
    {
        sum += num;
    }

    flag = true;
    i = num;

    while (flag && num <= end)
    {
        is_prime = true;
        i++;
        fseek(fptr, 0, SEEK_SET);
        while (fscanf(fptr, "%llu", &num) != EOF)
        {
            if(i % num == 0)
            {
                is_prime = false;
                break;
            }
        }

        if (is_prime)
        {
            sum += i;
            fprintf(fptr, "%llu\n", i);
        }

        if(i == end)
        {
            flag = false;
        }
    }

    printf("%llu\n", sum);
    fclose(fptr);

    return 0;
}