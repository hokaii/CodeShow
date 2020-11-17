#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef char TElemType;
typedef struct{
	TElemType *elem;//0号单元闲置 
	int lastIndex;//二叉树最后一个结点的编号 
} SqBiTree;//顺序存储的二叉树

bool is_Desendant(SqBiTree T, int u, int v){
	//判断v结点是否是u结点的子孙 
	if(u<1 || v<1 || u>T.lastIndex || v>T.lastIndex || u>=v)
		return false;
	while(v>u){
		v = v/2;
		if(v == u)
			return true;
	}
	return false;
} 
