#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	int num, first, second, mul = 0, length, temp, flag, digits = 0;
	printf("Enter the limit number.\n");
	scanf("%i", &num);
	temp = num;

	while (temp != 0)
	{
		temp /= 10;
		digits++;
	}

	char mul_c[2 * digits];

	for (first = num; first >= pow(10,digits-1); --first)
	{
		for (second = num; second >= pow(10,digits-1); --second)
		{
			flag = 0;
			sprintf(mul_c, "%i", first * second);

			for (int i = 0, length = strlen(mul_c); i < length / 2; ++i)
			{
				if (mul_c[i] != mul_c[length - (i + 1)])
				{
					flag = 1;
					break;
				}
			}
			if (first * second > mul && flag == 0)
				mul = first * second;

		}
	}

	printf("%i\n", mul);
	
	system("pause");
	return 0;
}