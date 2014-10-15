#include <stdio.h>
#include <stdlib.h>

/* check http://www.robertdickau.com/lattices.html
 * and http://www.robertdickau.com/manhattan.html
 */

#define N 20

int main(int argc, char const *argv[])
{
    int i, j;
    unsigned long long int* triangle[(2 * N) + 1];
    for (i = 0; i < (2 * N) + 1; ++i)
    {
        triangle[i] = (unsigned long long int*) malloc((i+1) * sizeof(unsigned long long int));
        
        triangle[i][0] = 1;
        triangle[i][i] = 1;
        for (j = 1; j < i; ++j)
        {
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
        }
    }

    printf("%llu\n", triangle[2 * N][N]);
    return 0;
}