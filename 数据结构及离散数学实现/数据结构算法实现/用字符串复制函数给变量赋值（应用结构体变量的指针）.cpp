//主要学习应用字符串复制函数将字符复制给变量 
#include <stdio.h>
#include <string.h>
int main()
{
	struct student
	{
		long num;
		char name[20];
		char sex;
		float score;
	};
	struct student stu_1;
	struct student *p;
	p=&stu_1;
	stu_1.num=10101;
	strcpy(stu_1.name,"li lin");   //注意该处 
	stu_1.sex='m';
	stu_1.score=89.5;
	printf("no.%ld\nname:%s\nsex:%c\nscore:%5.1f\n",stu_1.num,stu_1.name,stu_1.sex,stu_1.score);
	printf("no.%ld\nname:%s\nsex:%c\nscore:%5.1f\n",(*p).num,(*p).name,(*p).sex,(*p).score);
	return 0;
}
