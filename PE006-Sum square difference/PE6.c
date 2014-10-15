#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(void)
{
	int sum_of_squares, square_of_sum, sum;
	sum = 0;
	sum_of_squares = 0;

	for (int i = 1; i <= 100; ++i)
	{
		sum += i;
		sum_of_squares += ceil(pow((double) i, 2));
	}

	square_of_sum = ceil(pow((double) sum, 2));

	printf("%d\n", square_of_sum - sum_of_squares);
	
	system("pause");
	return 0;
}