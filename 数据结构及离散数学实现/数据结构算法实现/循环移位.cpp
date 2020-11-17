#include <stdio.h>
int main()
{
	int i,j,k,n;
	int count=1;
	printf("please enter an interger number:");
	scanf("%d",&j);
	while(j/10>0)
	{
		count++;
		j=j/10;
	}
	printf("please enter the number again:)");
	int a[count],b[count];
	for(i=0;i<count;i++)
	scanf("%1d",&a[count]);
    printf("please enter the number of displacement:");
    scanf("%d",n);
    for(i=0;i<count;i++)
	{
	if(i+2<=count)
	b[i]=a[i+2];
	else
	b[i]=a[i-2];
    }
    printf("the result is:");
    for(i=0;i<count;i++)
    printf("%d",b[i]);
    return 0;
}
