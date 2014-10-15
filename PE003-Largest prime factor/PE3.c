#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	unsigned long long number, max_factor;
	printf("Enter the number you want to factorize.\n");
	scanf("%lli", &number);

	while (number > 1)
	{
		for (unsigned long long i = 2; i <= number; ++i)
		{
			if (number % i == 0)
			{
				number = number / i;
				max_factor = i;
				break;
			}
		}
	}

	printf("%lli\n", max_factor);
	
	system("pause");
	return 0;
}