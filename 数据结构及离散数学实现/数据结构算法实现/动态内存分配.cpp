动态内存分配与指向它的指针变量
1.建立内存的动态分配
（1）建立malloc函数
     原型为：void *malloc(unsigned int size);
     +
	 其作用是在内存的动态存储区中分配一个长度为size的连续空间。形参size的类型定为无符号整型。此函数的值（即“返回值”）是所分配区域的第一个字节
	 的地址，或者说，此函数是一个指针型函数，返回的指针指向该分配域的开头位置。如：
	 malloc（100）         //开辟100字节的临时分配域，函数值为其第一个字节的地址
	 注意指针的基类型为void，即只提供一个地址。如果函数未能成功执行，则返回空指针（NULL）。
（2）使用calloc函数
     原型为：void *calloc(unsigned n,unsigned size);
	 其作用是在内存的动态存储区中分配n个长度为size的连续空间，这个空间一般比较大，足以保存一个数组
（3）使用free函数
     原型为：void *realloc(void *p,unsigned int size);
     其作用是释放指针变量p所指的动态空间，使这部分空间能重新被其他变量使用。p应是最近一次调用calloc或者malloc函数时得到的函数返回值。如：
	 free(p);
	 free函数无返回值
（4）使用recalloc函数
     原型为：void *realloc(void *p,unsigned int size); 
	 如果已经通过malloc函数或者calloc函数获得了动态空间，想改变其大小，可以用realloc函数重新分配.如：
	 realloc(p,50);         //返回字符型数据的指针 
	 
例：建立动态数组，输入5个学生的成绩，另外用一个函数检查其中有无低于60分的，输出不合格的成绩

思路：用malloc函数开辟一个动态自由区域，用来存5个学生的成绩，会得到这个动态区域第一个字节的地址，它的基类型是void型。用一个基类型为int的指针变量
      p来指向动态数组的各元素，并输出它们的值。但必须先把malloc函数返回的void指针转换为整型指针，然后赋给p1.
	  
程序：
    #include <stdio.h>
	#include <stdlib.h>                             //程序中用了malloc函数，应包含stdlib。h                              
	int main()
	{
		void check(int *);
		int *p1,i;
		p1=(int *)malloc(5*sizeof(int));           //开辟动态内存区，将地址转换为int *型，然后放在p1中 
		for(i=0;i<5;i++)
		scanf("%d",p1+i);
		check(p1);
		return 0;
	}
	
	void check(int *p)
	{
		int i;
		pritnf("they are fail:");
		for(i=0;i<5;i++)
		if(p[i]<60)
		printf("%d",p[i]);
		printf("\n");
	}
