#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// link with -lm

int main(void)
{
    FILE* fptr;
    if ((fptr = fopen("grid.txt", "r")) == NULL)
    {
        printf("Error opening the grid. Exiting...\n");
        return 1;
    }

    int i, j, r, c;
    short int num, grid[20][20];
    unsigned int max_product = 0, product;
    char way[4];

    for (i = 0; i < 20; ++i)
    {
        for (j = 0; j < 20; ++j)
        {
            fscanf(fptr, "%2hd", &num);
            grid[i][j] = num;
            if (j % 20 != 0)
            {
                fseek(fptr, 1, SEEK_CUR);
            }
        }
    }

    // checking horizontally
    for (i = 0; i < 20; ++i)
    {
        for (j = 0; j < 17; ++j)
        {
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3];
            if (product > max_product)
            {
                r = i;
                c = j;
                max_product = product;
                sprintf(way, "hor");
            }
        }
    }

    // checking vertically
    for (j = 0; j < 20; ++j)
    {
        for (i = 0; i < 17; ++i)
        {
            product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j];
            if (product > max_product)
            {
                r = i;
                c = j;
                max_product = product;
                sprintf(way, "ver");
            }
        }
    }

    // checking diagonally
    for (i = 0; i < 17; ++i)
    {
        for (j = 0; j < 17-i; ++j)
        {
            // upper diagonals
            product = grid[j][j+i] * grid[j+1][j+i+1] * grid[j+2][j+i+2] * grid[j+3][j+i+3];
            if (product > max_product)
            {
                r = j;
                c = j+i;
                max_product = product;
                sprintf(way, "dia");
            }
            if (i != 0)
            {
                // lower diagonals
                product = grid[j+i][j] * grid[j+i+1][j+1] * grid[j+i+2][j+2] * grid[j+i+3][j+3];
                if (product > max_product)
                {
                    r = j+i;
                    c = j;
                    max_product = product;
                    sprintf(way, "dia");
                }
            }
            
        }
    }

    // checking anti-diagonally
    for (i = 0; i < 17; ++i)
    {
        for (j = 0; j < 17-i; ++j)
        {
            // upper anti-diagonals
            product = grid[19-i-j][j] * grid[19-i-j-1][j+1] * grid[19-i-j-2][j+2] * grid[19-i-j-3][j+3];
            if (product > max_product)
            {
                r = 19-i-j;
                c = j;
                max_product = product;
                sprintf(way, "adi");
            }
            if (i != 0)
            {
                // lower anti-diagonals
                product = grid[19-j][j+i] * grid[19-j-1][j+i+1] * grid[19-j-2][j+i+2] * grid[19-j-3][j+i+3];
                if (product > max_product)
                {
                    r = 19-j;
                    c = j+i;
                    max_product = product;
                    sprintf(way, "adi");
                }
            }
        }
    }

    printf("%d at %d,%d %s\n", max_product, r, c, way);
    return 0;
}