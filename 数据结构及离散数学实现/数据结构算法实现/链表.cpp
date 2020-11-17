链表相关内容
1.静态链表 
#include <stdio.h>
struct student
{
	int num;
	float score;
	struct student * next;
};
int main()
{
	struct student a,b,c,*head,*p;
	a.num=10101;a.score=89.5;
	b.num=10103;b.score=90;
	c.num=10107;c.score=85;
	head=&a;
	a.next=&b;
	b.next=&c;
	c.next=NULL;
	p=head;
	do
	{
		printf("%ld %5.1f\n",p->num,p->score);         //输出p指向的结点的数据 
		p=p->next;                                     //使p指向下一结点 
	}
	while(p!=NULL);                                    //输出完c结点后p的值为NULL，循环终止 
	return 0; 
}

2.建立动态链表
例：写一函数建立一个有3名学生数据的单向动态链表。
（相关内容：动态内存分配）

思路：
    定义三个指针变量：head,p1和p2，它们都是用来指向struct student类型数据的。先用malloc函数开辟第一个结点，并使p1和p2指向它。然后从键盘读入一个学生的数据给
p1所指向的第一个结点。在此约定学号不会为零，如果输入的学号为零，则表示建立链表的过程完成，该节点不应连接到链表中。先使head的值为NULL（即等于0），这是链
表为“空”时的情况（即head不指向任何结点，即链表中无结点），当建立第一个结点就使head指向该节点。
    如果输入的p1->num不等于0，则输入的是第一个结点数据（n=1），令head=p1，即把p1的值赋给head，也就是使head也指向新开辟的结点。p1所指向的新开辟的结点就成为
链表中第一个结点。然后再开辟另一个结点并使p1指向它，接着输入该结点的数据。
    如果输入的p1->num不等于0.则应链入第二个结点（n=2），由于n不等于1，则将p1的值赋给p2->next，此时p2指向第一个结点，因此执行“p2->next=p1”就将新节点的地址
赋给第一个结点的next成员，使第一个结点的next成员指向第二个结点。接着使p2=p1，也就是使p2指向刚才建立的结点。
    再开辟一个新节点，并使p1指向它，输入该节点的数据。在第三次循环中，由于n=3，又将p1的值赋给p2->next，也就是将第三个结点连接到第二个结点之后，并使p2=p1，使
p2指向最后一个结点。 
	再开辟一个新节点，并使p1指向它，输入该节点的数据。由于p1->num的值为0，不再执行循环，此新节点不应被连接到链表中。此时将NULL赋给p2->next。建立链表过程到此
结束，p1最后指向的结点未链入链表中，第三个结点的next成员的值为NULL，它不指向任何结点。虽然p1指向新开辟的结点，但从链表中无法找到该结点。    

#include <stdio.h>
#include <stdlib.h>
#define len sizeof(struct student)
struct student
{
	long num;
	float score;
	struct student * next;
};
int n;                                             //n为全局变量 
struct student * creat(void)                       //定义函数，此函数返回一个指向链表头的指针 
{                                                  //建立链表的函数 
	struct student * head;
	struct student *p1,*p2;
	n=0;            
	p1=p2=(struct student * ) malloc(len);         //开辟一个新单元 
	scanf("%ld,%f",&p1->num,&p1->score);
	head=NULL;
	while(p1->num!=0)
	{
		n=n+1;
		if(n==1)
		head=p1;
		else
		p2->next=p1;
		p2=p1;
		p1=(struct student * )malloc(len);         //开辟动态存储区，把起始地址赋给p1
		scanf("%ld,%f",&p1->num,&p1->score);       //输入其他学生的学号和成绩 
	}
	p2->next=NULL;
	return(head);
}
void print(struct student *head)                   //输出链表的函数 
{
	struct student *p;
	printf("\nnow.these %d records are :\n",n);
	p=head;
	if(head!=NULL)
	do
	{
		printf("%ld  %5.1f\n",p->num,p->score);
		p=p->next;
	}while(p!=NULL);
} 
void main()
{
	struct student * head;
	head=creat();
    print(head); 
} 


