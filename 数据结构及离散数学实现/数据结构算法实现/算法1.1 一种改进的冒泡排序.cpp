#include <stdio.h>
void bubbleSort(int a[],int n);

void bubbleSort(int a[],int n)
{
	int i,j,temp;
	status change=TRUE;
	for(i=n-1;i>1&&change;--i)
	{
		change=FALSE;
		for(j=0;j<i;++j)
			if(a>[j]>a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
				change=TRUE;
			}
	}
}

int main()
{
	int a[10]={3,3,324,235445,6434,2323534,554};
	bubbleSort(a,10);
 } 
