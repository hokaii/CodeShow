#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef char TElemType;
typedef struct{
	TElemType *elem;//0�ŵ�Ԫ���� 
	int lastIndex;//���������һ�����ı�� 
} SqBiTree;//˳��洢�Ķ�����

bool is_Desendant(SqBiTree T, int u, int v){
	//�ж�v����Ƿ���u�������� 
	if(u<1 || v<1 || u>T.lastIndex || v>T.lastIndex || u>=v)
		return false;
	while(v>u){
		v = v/2;
		if(v == u)
			return true;
	}
	return false;
} 
