//дһ���ж������ĺ�����������������һ������������Ƿ�Ϊ��������Ϣ
#include <stdio.h>
int main()
{
	int sushu(int a);
	int a;
	printf("please enter a number:\n");
	scanf("%d",&a);
    if(sushu(a)==0)
	printf("�������������\n");
	else
	printf("�����������\n"); 
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
