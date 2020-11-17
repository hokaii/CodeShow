#include <stdio.h>
int main()
{
	int a[20];
	int i,k,l;
	printf("please enter a interger number:");
	scanf("%d",&k);
	for(i=0;;i++)
	{
		a[i]=k%2;
		k=k/2;
		if(k==1)
		{
			l=i+1;
			a[i+1]=1;
			break;
		}
	}
	printf("the interger number is:");
	for(i=l;i>=0;i--)
	printf("%d",a[i]);
}
