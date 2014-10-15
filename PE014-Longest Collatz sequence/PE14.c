#include <stdio.h>
#include <stdlib.h>

#define LIMIT 1000000

int main(int argc, char const *argv[])
{
    unsigned int i, num, terms, max_terms = 0, max_number;

    for (i = 1; i <= LIMIT; ++i)
    {
        terms = 1;
        num = i;
        while (num != 1)
        {
            terms++;
            if (num % 2 == 1)
            {
                num = (num * 3) + 1;
            }
            else
            {
                num = num / 2;
            }
        }

        if (terms > max_terms)
        {
            max_terms = terms;
            max_number = i;
        }
    }

    printf("Number with maximum terms: %d, with %d terms.\n", max_number, max_terms);
    return 0;
}