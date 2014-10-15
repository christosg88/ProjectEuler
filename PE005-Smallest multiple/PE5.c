#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	int flag = 1;
	int num = 19;
	while (flag)
	{
		flag = 0;
		num++;
		for (int i = 1; i <= 20; ++i)
		{
			if (num % i != 0)
			{
				flag = 1;
				break;
			}
		}
	}
	printf("%i\n", num);
	
	system("pause");
	return 0;
}