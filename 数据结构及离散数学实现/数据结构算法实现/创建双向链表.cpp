//ʵ��˵������ʵ��ʵ�ִ���һ��˫���������������������������������У�����Ҫ���ҵ�ѧ�����֣������ҵ�������������ɾ��������ʾɾ��������� 
#include <stdio.h>
#include <malloc.h> 
#include <string.h>
#include <conio.h>
typedef struct node
{
	char name[20];
	struct node *prior, *next;
}stud;                                                    //˫����Ľṹ����
 
stud *creat(int n)
{
	stud *p, *h, *s;                                      //��Ҫ����ָ�������h��¼�����ʼ��ͷ��ַ��p����ѭ�����ӽ�㣬s��������nameͬʱ���Ƽ��ص�p�� 
	int i;
	h=(stud*)malloc(sizeof(stud));                        //������ռ� 
	h->name[0]='\0';
	h->prior=NULL;
	h->next=NULL;
	p=h;
	for(i=0;i<n;i++)
	{
		s=(stud*)malloc(sizeof(stud));
		p->next=s;                                        //ָ����̽��  
		printf("input the %d student's name:",i+1);
		scanf("%s",s->name);
		s->prior=p;                                       //ָ��ǰ����� 
		s->next=NULL;
		p=s;
	}
	p->next=NULL;
	return (h);
}

stud *search(stud *h,char *x)
{
	stud *p;                                              //ָ��ṹ�����͵�ָ�� 
	char *y;
	p=h->next;
	while(p)
	{
		y=p->name;
		if(strcmp(y,x)==0)                                //�����Ҫɾ���Ľ�㣬�򷵻ص�ַ  
		return (p);
		else 
		p=p->next;
	}
	printf("cannot find data!\n");
}

void del(stud *p)
{
	p->next->prior=p->prior;                              //p����һ������ǰ��ָ��ָ��p��ǰ����� 
	p->prior->next=p->next;                               //p��ǰ�����ĺ��ָ��ָ��p�ĺ��ָ�� 
	free(p);
}

int main()
{
	int number;
	char sname[20];
	stud *head, *sp;
	puts("Please input the size of the list:");
	scanf("%d",&number);                                   //������������ 
	head=creat(number);                                    //�������� 
	sp=head->next;
	printf("\nNow the double list is:\n");
	while(sp)                                              //������������� 
	{
		printf("%s",&*(sp->name));
		sp=sp->next;
	}
	printf("\nPlease input the name which you want to find:\n");
	scanf("%s",sname);
	sp=search(head,sname);                                 //����ָ����� 
	printf("the name you want to find is:%s\n", *&sp->name);
	del(sp);                                               //ɾ����� 
	sp=head->next;
	printf("Now the double list is:\n");
	while(sp)
	{
		printf("%s",&*(sp->name));                         //�����ǰ���������� 
		sp=sp->next;
	} 
	printf("\n");
	puts("\n Press any key to quit...");
	getch();
} 
