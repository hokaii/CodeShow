//写一个判断素数的函数，在主函数输入一个整数，输出是否为素数的信息
#include <stdio.h>
int main()
{
	int sushu(int a);
	int a;
	printf("please enter a number:\n");
	scanf("%d",&a);
    if(sushu(a)==0)
	printf("这个数不是素数\n");
	else
	printf("这个数是素数\n"); 
	return 0;
} 


int sushu(int a)
{
	int i,j;
	j=1;
	for(i=2;i<a;i++)
	{
		if(a%i==0)
        {
        	j=0;
		    break;
		}
	}
	return(j);
}
