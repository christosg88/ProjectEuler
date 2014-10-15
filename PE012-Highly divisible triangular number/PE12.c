#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

int main(int argc, char const *argv[])
{
    int factors;
    unsigned long long int i, sum = 0, count = 1;
    bool flag = true;

    while (flag)
    {
        factors = 1;
        sum += count;
        count++;
        for (i = 1; i <= sum/2; ++i)
        {
            if (sum % i == 0)
            {
                factors++;
            }
        }

        if (factors > 500)
        {
            flag = false;
        }

    }

    printf("Triangular number with at least 500 divisors: %llu\n", sum);

    return 0;
}