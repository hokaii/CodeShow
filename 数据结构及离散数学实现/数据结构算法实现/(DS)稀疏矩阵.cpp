#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef struct{
	int i,j;//����Ԫ���к��� 
	int e;//����Ԫ��ֵ 
} Triple;//��Ԫ�� 

typedef struct{
	Triple data[MAXSIZE+1];//����Ԫ��Ԫ���,0�ŵ�Ԫδ�� 
	int mu,nu,tu;//���������,�����ͷ���Ԫ�ĸ��� 
} TSMatrix;//��Ԫ��˳���

int CreateSMatrix(TSMatrix &M){
	int i,m,n,e,k;
	printf("���ڹ�����Ԫ��˳����������������������������Ԫ�ظ���\n");
	scanf("%d,%d,%d",&M.mu,&M.nu,&M.tu);
	M.data[0].i = 0;
	M.data = (Triple*)malloc(sizeof(Triple)*3);
	if(M.data == NULL)
		printf("OVERFLOW");
	for(int i=0;i<)
}
