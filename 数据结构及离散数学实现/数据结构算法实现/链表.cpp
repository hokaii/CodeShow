�����������
1.��̬���� 
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
		printf("%ld %5.1f\n",p->num,p->score);         //���pָ��Ľ������� 
		p=p->next;                                     //ʹpָ����һ��� 
	}
	while(p!=NULL);                                    //�����c����p��ֵΪNULL��ѭ����ֹ 
	return 0; 
}

2.������̬����
����дһ��������һ����3��ѧ�����ݵĵ���̬����
��������ݣ���̬�ڴ���䣩

˼·��
    ��������ָ�������head,p1��p2�����Ƕ�������ָ��struct student�������ݵġ�����malloc�������ٵ�һ����㣬��ʹp1��p2ָ������Ȼ��Ӽ��̶���һ��ѧ�������ݸ�
p1��ָ��ĵ�һ����㡣�ڴ�Լ��ѧ�Ų���Ϊ�㣬��������ѧ��Ϊ�㣬���ʾ��������Ĺ�����ɣ��ýڵ㲻Ӧ���ӵ������С���ʹhead��ֵΪNULL��������0����������
��Ϊ���ա�ʱ���������head��ָ���κν�㣬���������޽�㣩����������һ������ʹheadָ��ýڵ㡣
    ��������p1->num������0����������ǵ�һ��������ݣ�n=1������head=p1������p1��ֵ����head��Ҳ����ʹheadҲָ���¿��ٵĽ�㡣p1��ָ����¿��ٵĽ��ͳ�Ϊ
�����е�һ����㡣Ȼ���ٿ�����һ����㲢ʹp1ָ��������������ý������ݡ�
    ��������p1->num������0.��Ӧ����ڶ�����㣨n=2��������n������1����p1��ֵ����p2->next����ʱp2ָ���һ����㣬���ִ�С�p2->next=p1���ͽ��½ڵ�ĵ�ַ
������һ������next��Ա��ʹ��һ������next��Աָ��ڶ�����㡣����ʹp2=p1��Ҳ����ʹp2ָ��ղŽ����Ľ�㡣
    �ٿ���һ���½ڵ㣬��ʹp1ָ����������ýڵ�����ݡ��ڵ�����ѭ���У�����n=3���ֽ�p1��ֵ����p2->next��Ҳ���ǽ�������������ӵ��ڶ������֮�󣬲�ʹp2=p1��ʹ
p2ָ�����һ����㡣 
	�ٿ���һ���½ڵ㣬��ʹp1ָ����������ýڵ�����ݡ�����p1->num��ֵΪ0������ִ��ѭ�������½ڵ㲻Ӧ�����ӵ������С���ʱ��NULL����p2->next������������̵���
������p1���ָ��Ľ��δ���������У�����������next��Ա��ֵΪNULL������ָ���κν�㡣��Ȼp1ָ���¿��ٵĽ�㣬�����������޷��ҵ��ý�㡣    

#include <stdio.h>
#include <stdlib.h>
#define len sizeof(struct student)
struct student
{
	long num;
	float score;
	struct student * next;
};
int n;                                             //nΪȫ�ֱ��� 
struct student * creat(void)                       //���庯�����˺�������һ��ָ������ͷ��ָ�� 
{                                                  //��������ĺ��� 
	struct student * head;
	struct student *p1,*p2;
	n=0;            
	p1=p2=(struct student * ) malloc(len);         //����һ���µ�Ԫ 
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
		p1=(struct student * )malloc(len);         //���ٶ�̬�洢��������ʼ��ַ����p1
		scanf("%ld,%f",&p1->num,&p1->score);       //��������ѧ����ѧ�źͳɼ� 
	}
	p2->next=NULL;
	return(head);
}
void print(struct student *head)                   //�������ĺ��� 
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


