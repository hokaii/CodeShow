#include <stdio.h>
void to(unsigned long n);

int main()
{
	unsigned long n;
	printf("enter an interger (q to quit):\n");
	while(scanf("%d",&n)==1)
	{
		printf("binary equivalent: ");
		to(n);
		putchar('\n');
		printf("enter an interger (q to quit):\n");
	}
	printf("bye.\n");
	return 0;
}

void to(unsigned long n)
{
	int r;
	r=n%2;
	if(n>=2)
	to(n/2);
	putchar(r==0?'0':'1');
	return;
}
