#include <stdio.h>                                #include <stdio.h>
int main()                                        int main()
{                                                 {   
	char a[]="i am a student!",b[20];                 char a[]="i am a student!",b[20]; 
	char *p,*q;                                       int i;
	p=a;                                              for(i=0;*(a+i)!='\0';i++)
	q=b;                                              *(b+i)=*(a+i);
	for(;*p!='\0';p++,q++)                            *(b+i)='\0';
	*q=*p;                                            printf("string a is :%s\n",a);
	*q='\0';                                          printf("string b is :");
	printf("string a is :%s\n",a);                    for(i=0;*(b+i)!='\0';i++)
	printf("string b is :%s\n",b);                    printf("%c",*(b+i));
	return 0;                                         return 0;
}                                                  }


�ַ�ָ������������
1.���ַ���������Ϊ��������                         2.���ַ���ָ�������ʵ��                           3.���ַ�ָ��������βκ�ʵ�� 
#include <stdio.h>                                 #include <stdio.h>                                 #include <stdio.h> 
int main()                                         int main()                                         int main()
{                                                  {                                                  {
	void copy(char from[],char to[]);                   void copy(char from[],char to[]);                  void copy(char *from,char *to);
	char a[]="i am a student!";                         char a[]="i am a student!";                        char *a="i am a student!";
	char b[]="you are a teacher!";                      char b[]="i am a teacher!";                        char b[]="you are a teacher!";
	printf("string a=%s\nstring b=%s\n",a,b);           char *from=a.*to=b;                                char *p=b;
	copy(a,b);                                          printf("string a=%s\nstring b=%s\n",a,b);          printf("string a=%s\nstring b=%s\n",a,b);
	printf("copy string a to string b:\n");             printf("\ncopy string a to string b:\n");          printf("\ncopy string a to string b:\n");
	printf("\nstring a=%s\nstring b=%s\n",a,b);         copy(from,to);                                     copy(a,p);
	return 0;                                           printf("string a =%s\nstring b=%s\n",a,b);         printf("string a=%s\nstring b=%s\n",a,b);
}                                                       return 0;                                          return 0;
                                                   }                                                  }

void copy(char from[],char to[])                   void copy(char from[],char to[])                   void copy(char *from,char *to)
{                                                  {                                                  {
	int i=0;                                            int i=0;                                           for(;*from!='\0';from++,to++)
	while(from[i]!='\0')                                while(from[i]!='\0');                              {
	{                                                   {                                                        *to=*from;
		to[i]=from[i];                                       to[i]=from[i];                                }
		i++;                                                 i++;                                          *to='\0';
	}                                                   }                                             }
	to[i]='\0';                                         to[i]='\0';
}                                                  }
1.��1��2�ȽϿɵã����ַ���������������ʱ�����ǽ�����ĵ�ַ��������
2.ʹ���ַ�ָ��������ַ�����ıȽ�
  ��1���ַ����������ɸ�Ԫ����ɣ�ÿ��Ԫ���д��һ���ַ������ַ�ָ������д�ŵ��ǵ�ַ�������ǽ��ַ����ŵ��ַ�ָ�������
  ��2����ֵ��ʽ�����Զ��ַ�ָ�������ֵ�������ܶ���������ֵ
       ���Բ������淽�����ַ�ָ�������ֵ��
	   char *a;          //aΪ�ַ�ָ����� 
	   a="i love china!"; //���ַ�����Ԫ�ص�ַ����ָ��������Ϸ���������a�Ĳ����ַ����������ַ�����һ��Ԫ�صĵ�ַ
	   ���������·������ַ���������ֵ��
	   char str[4];          //
	   str[0]='I';           //���ַ�����Ԫ�ظ�ֵ���Ϸ� 
	   str="i love china!"   //�������ǵ�ַ���ǳ��������ܱ���ֵ���Ƿ�
   (3) ��ʼ���Ķ��塣���ַ�ָ���������ֵ��
       char *a="i love china!";
	   �ȼ���
	   char *a;
	   a="i love china!";
	   ��������ĳ�ʼ��
	   char str[14]="i love china!";
	   ���ȼ���
	   char str[14];
	   str[]="i love china!";
	   ��������ڶ���ʱ�Ը�Ԫ�ظ���ֵ���������ø�ֵ�����ַ�������ȫ��Ԫ�����帳ֵ��
  ��4��ָ�������ֵ�ǿ��Ըı�ģ�������������һ���̶���ֵ��������Ԫ�صĵ�ַ�������ܸı�
       �����ı�ָ�������ֵ
       #include <stdio.h>
       int main()
       {
       	   char *a="i love china!";
       	   a=a+7��                        //�ı�ָ�������ֵ�����ı�ָ�������ָ�� 
		   printf("%s\n",a)               //�����aָ����ַ���ʼ���ַ��� 
		   return 0; 
	   }
	   
	   ���н���� china!
   (5) �ַ������и�Ԫ�ص�ֵ�ǿ��Ըı�ģ����Զ������ٸ�ֵ�������ַ�ָ�����ָ����ַ��������е������ǲ����Ա�ȡ���ģ����ܶ������ٸ�ֵ�����磺
       char a[]="house";       //�ַ�����a��ʼ�� 
	   char *b="house";        //�ַ�ָ�����bָ���ַ��������ĵ�һ���ַ� 
	   a[2]='r';               //�Ϸ���rȡ��a����Ԫ��a[2]��ԭֵu 
	   b[2]='r'                //�Ƿ����ַ����������ܴ���
  ��6����ָ�����ָ��һ����ʽ�ַ�����������������printf�����еĸ�ʽ�ַ��������磺
       char *format;
	   format="a=%d,b=%f\n";
	   printf(format,a,b);
	   ���൱��
	   printf("a=%d,b=%d",a,b);
	   ����printf������Ϊ�ɱ��ʽ�������
	   Ҳ�������ַ�����ʵ�֣����磺
	   char format[]="a=%d,b=%f\n";
	   printf(format,a,b); 
	   
	   


ָ������
��һ�������ȫ��Ԫ�ؾ�Ϊָ���������ݣ�����int *p[4];
�ʺ�����ָ�����ɸ��ַ�����ʹ�ַ���������ӷ�����
�����������ַ�������ĸ˳����С�������
#include <stdio.h>
#include <string.h>
int main()
{
	void sort(char *name[],int n);
	void print(char *name[],int n);
	char *name[]={"Follow me","BASIC","Great Wall","FORTRAN","Computer design"};
    int n=5;
    sort(name,n);
    print(name,n);
    return 0;
}


void sort(char *name[],int n)
{
	char *temp;
	int i,j,k;
	for(i=0;i<n-1;i++)
	{
		k=i;
		for(j=i+1;j<n;j++)
		if(strcmp(name[k],name[j])>0)
		k=j;
		if(k!=i)
		{
			temp=name[i];name[i]=name[k];name[k]=temp;
		}
	}
}

                                         print����Ҳ���Ը�дΪ������ʽ�� 
void print(char *name[],int n)           void print(char *name[],int n)    
{                                        {
	int i;                                    int i=0;
	for(i=0;i<n;i++)                          char *p;
	printf("%s\n",name[i]);                   p=name[0];
}                                             while(i<n)
                                              {
											      p=*(name+i++);
											      printf("%s\n",p);
										      }
							             }
							            ���С�*��name+i++������ʾ����
										*��name+i)��ֵ����name[i]�����Ǹ���ַ����
										Ȼ��ʹi��1.�����ʱ�����ַ�����ʽ�����p
										��ַ��ʼ���ַ��� 
									     
��������3���ַ���������С�����˳�������
#include <stdio.h>
#include <string.h>
int main()
{
	void swap(char *,char *);
	char str1[20],str2[31],str3[20];
	printf("input three line:\n");
	gets(str1);
	gets(str2);
	gets(str3);
	if(strcmp(str1,str2)>0)
	swap(str1,str2);
	if(strcmp(str1,str3)>0)
	swap(str1,str3);
	if(strcmp(str2,str3)>0)
	swap(str2,str3);
	printf("now,the order is:\n");
	printf("%s\n%s\n%s\n",str1,str2,str3);
	return 0;
}

void swap(char *p1,char *p2)
{
	char p[20];
	strcpy(p,p1);
	strcpy(p1,p2);
	strcpy(p2,p);
 } 									     
									     
��������������10���ȳ����ַ���������һ��������������Ȼ���������������10���Ѿ��ź�����ַ�
#include <stdio.h>
#include <string.h>
int main()
{
	void sort(char s[][6]);
	int i;
	char str[10][6];
	printf("input 10 strings:\n");
	for(i=0;i<10;i++)
	scanf("%s",str[i]);
	sort(str);
	printf("now,the sequence is:\n");
	for(i=0;i<10;i++)
	printf("%s\n",str[i]);
	return 0;
}

void sort(char s[10][6])
{
	int i,j;
	char *p,temp[10];
	p=temp;
	for(i=0;i<9;i++)
	 for(j=0;j<9-i;j++)
	   if(strcmp(s[j],s[j+1])>0)
	   {
	   	strcpy(p,s[j]);
	   	strcpy(s[j],s[+j+1]);
	   	strcpy(s[j+1],p);
	   }
}
