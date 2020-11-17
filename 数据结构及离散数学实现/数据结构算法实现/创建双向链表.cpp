//实例说明：本实例实现创建一个双向链表，并将这个链表中数据输出到窗体中，输入要查找的学生名字，将查找的姓名从链表中删除，并显示删除后的链表 
#include <stdio.h>
#include <malloc.h> 
#include <string.h>
#include <conio.h>
typedef struct node
{
	char name[20];
	struct node *prior, *next;
}stud;                                                    //双链表的结构定义
 
stud *creat(int n)
{
	stud *p, *h, *s;                                      //需要三个指针变量，h记录链表初始开头地址，p用来循环增加结点，s用来输入name同时复制加载到p上 
	int i;
	h=(stud*)malloc(sizeof(stud));                        //申请结点空间 
	h->name[0]='\0';
	h->prior=NULL;
	h->next=NULL;
	p=h;
	for(i=0;i<n;i++)
	{
		s=(stud*)malloc(sizeof(stud));
		p->next=s;                                        //指定后继结点  
		printf("input the %d student's name:",i+1);
		scanf("%s",s->name);
		s->prior=p;                                       //指定前驱结点 
		s->next=NULL;
		p=s;
	}
	p->next=NULL;
	return (h);
}

stud *search(stud *h,char *x)
{
	stud *p;                                              //指向结构体类型的指针 
	char *y;
	p=h->next;
	while(p)
	{
		y=p->name;
		if(strcmp(y,x)==0)                                //如果是要删除的结点，则返回地址  
		return (p);
		else 
		p=p->next;
	}
	printf("cannot find data!\n");
}

void del(stud *p)
{
	p->next->prior=p->prior;                              //p的下一个结点的前驱指针指向p的前驱结点 
	p->prior->next=p->next;                               //p的前驱结点的后继指针指向p的后继指针 
	free(p);
}

int main()
{
	int number;
	char sname[20];
	stud *head, *sp;
	puts("Please input the size of the list:");
	scanf("%d",&number);                                   //输入链表结点数 
	head=creat(number);                                    //创建链表 
	sp=head->next;
	printf("\nNow the double list is:\n");
	while(sp)                                              //输出链表中数据 
	{
		printf("%s",&*(sp->name));
		sp=sp->next;
	}
	printf("\nPlease input the name which you want to find:\n");
	scanf("%s",sname);
	sp=search(head,sname);                                 //查找指定结点 
	printf("the name you want to find is:%s\n", *&sp->name);
	del(sp);                                               //删除结点 
	sp=head->next;
	printf("Now the double list is:\n");
	while(sp)
	{
		printf("%s",&*(sp->name));                         //输出当前链表中数据 
		sp=sp->next;
	} 
	printf("\n");
	puts("\n Press any key to quit...");
	getch();
} 
