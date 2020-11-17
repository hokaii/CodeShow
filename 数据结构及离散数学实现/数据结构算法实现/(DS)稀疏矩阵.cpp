#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef struct{
	int i,j;//非零元的行和列 
	int e;//非零元的值 
} Triple;//三元组 

typedef struct{
	Triple data[MAXSIZE+1];//非零元三元组表,0号单元未用 
	int mu,nu,tu;//矩阵的行数,列数和非零元的个数 
} TSMatrix;//三元组顺序表

int CreateSMatrix(TSMatrix &M){
	int i,m,n,e,k;
	printf("正在构建三元组顺序表：请输入矩阵行数，列数，非零元素个数\n");
	scanf("%d,%d,%d",&M.mu,&M.nu,&M.tu);
	M.data[0].i = 0;
	M.data = (Triple*)malloc(sizeof(Triple)*3);
	if(M.data == NULL)
		printf("OVERFLOW");
	for(int i=0;i<)
}
