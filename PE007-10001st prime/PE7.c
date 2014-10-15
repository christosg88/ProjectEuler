#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    FILE* fptr;
    unsigned long long int i, j;
    unsigned int count;
    bool flag, is_prime;
    i = 2;
    flag = true;
    count = 1;
    if ((fptr = fopen("primes.txt", "w")) == NULL)
    {
        printf("Error creating the file. Exiting...");
        return 1;
    }
    
    fprintf(fptr, "%u. %llu\n", count, i);

    while (flag)
    {
        is_prime = true;
        i++;
        for(j = 2; j < i; ++j)
        {
            if(i % j == 0)
            {
                is_prime = false;
                break;
            }
        }

        if (is_prime)
        {
            count++;
            fprintf(fptr, "%u. %llu\n", count, i);
        }

        if(count == 1000000)
        {
            flag = false;
        }
    }

    fclose(fptr);
    return 0;
}