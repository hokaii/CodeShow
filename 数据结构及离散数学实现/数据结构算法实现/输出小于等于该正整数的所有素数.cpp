#include <stdio.h>
int main()
{
	int i,n,a;
	
	printf("请输入一个正整数:");
	scanf("%d",&a);
	if(a==1)
	printf("1");
	else
	printf("1\t");
	for(n=1;n<=a;n++)
	{
	   for(i=2;i<=n;i++)
	   if(n%i==0)
	   break;
	   if(i==n)
	   printf("%d\t",n);
	}
	return 0; 
}
