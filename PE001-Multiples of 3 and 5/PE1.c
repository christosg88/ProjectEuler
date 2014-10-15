/* Project Euler
 * Problem 1
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int sum = 0;

	for (int i = 0; i < 1000; ++i)
	{
		if (i % 3 == 0 || i % 5 == 0)
		{
			sum += i;
		}
	}
	printf("%i\n", sum);
	system("pause");
	return 0;
}