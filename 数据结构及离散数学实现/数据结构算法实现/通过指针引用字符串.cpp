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


字符指针作函数参数
1.用字符数组名作为函数参数                         2.用字符型指针变量作实参                           3.用字符指针变量作形参和实参 
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
1.由1和2比较可得：用字符数组作函数参数时，就是将数组的地址传给函数
2.使用字符指针变量和字符数组的比较
  （1）字符数组由若干个元素组成，每个元素中存放一个字符，而字符指针变量中存放的是地址，绝不是将字符串放到字符指针变量中
  （2）赋值方式。可以对字符指针变量赋值，但不能对数组名赋值
       可以采用下面方法对字符指针变量赋值：
	   char *a;          //a为字符指针变量 
	   a="i love china!"; //将字符串首元素地址赋给指针变量，合法。但赋给a的不是字符串，而是字符串第一个元素的地址
	   不能用以下方法对字符数组名赋值：
	   char str[4];          //
	   str[0]='I';           //对字符数组元素赋值，合法 
	   str="i love china!"   //数组名是地址，是常亮，不能被赋值，非法
   (3) 初始化的定义。对字符指针变量赋初值：
       char *a="i love china!";
	   等价于
	   char *a;
	   a="i love china!";
	   而对数组的初始化
	   char str[14]="i love china!";
	   不等价于
	   char str[14];
	   str[]="i love china!";
	   数组可以在定义时对各元素赋初值，但不能用赋值语句对字符数组中全部元素整体赋值。
  （4）指针变量的值是可以改变的，而数组名代表一个固定的值（数组首元素的地址），不能改变
       例：改变指针变量的值
       #include <stdio.h>
       int main()
       {
       	   char *a="i love china!";
       	   a=a+7；                        //改变指针变量的值，即改变指针变量的指向 
		   printf("%s\n",a)               //输出从a指向的字符开始的字符串 
		   return 0; 
	   }
	   
	   运行结果： china!
   (5) 字符数组中各元素的值是可以改变的（可以对它们再赋值），但字符指针变量指向的字符串变量中的内容是不可以被取代的（不能对它们再赋值）。如：
       char a[]="house";       //字符数组a初始化 
	   char *b="house";        //字符指针变量b指向字符串变量的第一个字符 
	   a[2]='r';               //合法，r取代a数组元素a[2]的原值u 
	   b[2]='r'                //非法，字符串变量不能代表
  （6）用指针变量指向一个格式字符串，可以用它代替printf函数中的格式字符串。例如：
       char *format;
	   format="a=%d,b=%f\n";
	   printf(format,a,b);
	   它相当于
	   printf("a=%d,b=%d",a,b);
	   这种printf函数称为可变格式输出函数
	   也可以用字符数组实现，例如：
	   char format[]="a=%d,b=%f\n";
	   printf(format,a,b); 
	   
	   


指针数组
即一个数组的全部元素均为指针类型数据，例：int *p[4];
适合用来指向若干个字符串，使字符串处理更加方便灵活。
例：将若干字符串按字母顺序（由小到大）输出
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

                                         print函数也可以改写为如下形式： 
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
							            其中“*（name+i++）”表示先求
										*（name+i)的值，即name[i]（它是个地址），
										然后使i加1.在输出时，按字符串形式输出从p
										地址开始的字符串 
									     
例：输入3个字符串，按由小到大的顺序输出。
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
									     
在主函数中输入10个等长的字符串。用另一函数对它们排序。然后在主函数输出这10个已经排好序的字符
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
