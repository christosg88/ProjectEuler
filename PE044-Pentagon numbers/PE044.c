/*Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten
pentagonal numbers are:
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 - 22 = 48, is not pentagonal.
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk - Pj| is minimized; what is the value
of D?*/

#include <stdio.h>
#include <math.h>

float myabs(float num);

int main(void)
{
    int n, i, flag;
    double D, S, x, y;

    n = 0;
    flag = 1;
    while (flag == 1)
    {
        n++;
        i = -1;
        while (myabs(i) < n)
        {
            D = myabs(((3*i*i) + (6*n*i) - i) / 2);
            x = (1 + (sqrt(1 + (24*D)))) / 6.0;
            if (x == floor(x))
            {
                S = ((6*n*n) + (3*i*i) + (6*n*i) - (2*n) - i) / 2;
                y = (1 + (sqrt(1 + (24*S)))) / 6.0;
                if (y == floor(y))
                {
                    printf("D = %d\nS = %d\nn = %d\n",(int) D , (int) S, n);
                    flag = 0;
                    break;
                }
            }
            i--;
        }
    }
    return 0;
}

float myabs(float num)
{
    if (num < 0)
    {
        return -num;
    }
    else
    {
        return num;
    }
}

/*5482660*/