#include <stdio.h>
int main()
{
	unsigned long num;      //待测试的数
	unsigned long div;      //可能的约数
	int isprime;
	
	printf("please enter an interger for ananlysis; ");
	printf("enter q to quit.\n");
	while(scanf("%lu",&num)==1)
	{
	for(div=2,isprime=1;(div*div)<=num;div++)
	{
		if(num%div==0)
		{
			if((div*div)!=num)
			printf("%lu is divisble by %lu and %lu.\n",num,div,num/div);
			else 
			printf("%lu is divisible by %lu.\n",num,div);
			isprime=0;       //该数不是素数 
		}
	}
	if(isprime)
	printf("%lu is prime.\n",num);
	printf("please enter anothter integer for analysis;");
	printf("enter q to quit.\n");
    }
    printf("bye.\n");
    return 0;
}
