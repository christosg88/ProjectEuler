#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
// link with -lm

int main(void)
{
    int c_squared;
    double c;

    for (int i = 1; i < 1000; ++i)
    {
        for (int j = 1; j < 1000; ++j)
        {
            c_squared = ceil(pow((double) i, 2)) + ceil(pow((double) j, 2));
            c = sqrt(c_squared);
            if (c == floor(c))
            {
                if (i + j + c == 1000)
                {
                    printf("%i\n", i*j*((int) c));
                    return 0;
                }
            }
        }
    }
    return 0;
}