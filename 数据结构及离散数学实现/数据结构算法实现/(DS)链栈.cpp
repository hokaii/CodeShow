#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef int ElemType;
typedef struct LSNode{
	ElemType data;//数据域 
	struct LSNode * next;//指针域 
}LSNode, *LStack;//结点和链栈类型

void InitStack_LS(LStack &S){
	S = (LStack)malloc(sizeof(LSNode));
	S -> next = NULL;
}

void DestroyStack_LS(LStack &S){
	LSNode *t;
	while(S->next != NULL){
		t = S;
		free(t);
		S = S->next;
	}
	free(S);
}

bool StackEmpty_LS(LStack S){
	if(NULL == S->next)
		return true;
	else
		return false;
}

int Push_LS(LStack &S, ElemType e){
	LSNode *t;
	t = (LSNode*)malloc(sizeof(LSNode));
	if(NULL == t)
		printf("OVERFLOW");
	t->data = e;
	t->next = S; 
	S = t;
	printf("push done\n");
	return OK;
}

int Pop_LS(LStack &S, ElemType &e){
	LSNode *t;
	if(NULL == S)
		return ERROR;
	t = S;
	e = S->data;
	S = S->next;
	free(t);
	return OK;
}

int GetTop_LS(LStack S, ElemType &e){
	e = S->data;
	return OK;
}

void Traverse_LS(LStack S){//遍历输出 
	LSNode *T = S;
	while(T->next!=NULL){
		printf("%d, ",T->data);
		T = T->next;
	}
}
/*
int main(){
	LStack S;
	int t;
	InitStack_LS(S);
	Push_LS(S, 12);
	Push_LS(S, 22);
	Push_LS(S, 23);
	Push_LS(S, 54);
	Pop_LS(S, t);
	printf("t is: %d\n", t);
	GetTop_LS(S, t);
	printf("t is: %d\n", t);
	printf("%d\n",StackEmpty_LS(S));
	Traverse_LS(S);
}*/
