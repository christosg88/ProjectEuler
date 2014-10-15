#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX 13

unsigned long long int product_f(int numbers[]);

int main(void)
{
    FILE* fptr;
    if ((fptr = fopen("number.txt", "r")) == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    int i, count;
    char c;
    unsigned long long int product, max_product;
    int numbers[MAX];

    max_product = 0;

    for (i = 0; i < 1000; ++i)
    {
        c = getc(fptr);
        if(c >= '0' && c <= '9')
        {
            numbers[i%MAX] = (int) (c - '0');
            if(i >= MAX - 1)
            {
                product = product_f(numbers);
                if(product > max_product)
                {
                    max_product = product;
                }
            }
        }
    }

    printf("%llu\n", max_product);
    fclose(fptr);
    return 0;
}

unsigned long long int product_f(int numbers[MAX])
{
    int i;
    unsigned long long int pro;
    pro = 1;
    for (int i = 0; i < MAX; ++i)
    {
        pro *= numbers[i];
    }

    return pro;
}