#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int first, second, next, limit, sum;
	first = 1;
	second = 1;
	next = first + second;
	sum = 0;
	printf("What's the upper limit?\n");
	scanf("%i", &limit);

	while (next < limit)
	{
		if (next % 2 == 0)
		{
			sum += next;
		}
		first = second;
		second = next;
		next = first + second;
	}
	printf("%i\n", sum);
	
	system("pause");
	return 0;
}