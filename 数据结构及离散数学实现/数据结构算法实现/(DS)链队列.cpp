#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef struct LQNode{
	int data;
	struct LQNode *next;
}LQNode;//结点及其指针类型 
typedef LQNode* QueuePtr;
typedef struct{
	QueuePtr front;
	QueuePtr rear;
} LQueue;//链队列

void InitQueue_LQ(LQueue &Q){
	Q.front = Q.rear = (QueuePtr)malloc(sizeof(LQNode));
	Q.front = NULL;
} 

void DestroyQueue_LQ(LQueue &Q){
	QueuePtr t = Q.front;
	while(t != Q.rear){
		t = Q.front;
		Q.front = Q.front->next;
		free(t);
	}
	free(Q.rear);
}

bool QueueEmpty_LQ(LQueue Q){
	if(Q.front == NULL)
		return true;
	else
		return false;
}

int QueueLength_LQ(LQueue Q){
	int i = 1;
	LQNode *t = Q.front;
	if(QueueEmpty_LQ(Q))
		return 0;
	else
		while(t != Q.rear){
			t = t->next;
			i++;
		}
	return i;
}

int GetHead_LQ(LQueue Q, int &e){
	if(QueueEmpty_LQ(Q))
		return ERROR;
	e = Q.front->data;
	return OK;
}

int EnQueue_LQ(LQueue &Q, int e){
	LQNode *t;
	t = (LQNode*)malloc(sizeof(LQNode));
	t->data = e;
	t->next = NULL;
	if(QueueEmpty_LQ(Q))
		Q.front = t;
	else
		Q.rear->next = t;
	Q.rear = t;
	return OK;
}

int DeQueue_LQ(LQueue &Q, int &e){
	if(QueueEmpty_LQ(Q))
		return ERROR;
	LQNode *t = Q.front;
	e = t->data;
	Q.front = Q.front->next;
	if(Q.rear == t){
		Q.rear = NULL;
	}
	free(t);
	return OK;
}

int main(){
	LQueue Q;
	int t;
	InitQueue_LQ(Q);
	printf("null of notnull: %d\n",QueueEmpty_LQ(Q));
	EnQueue_LQ(Q, 13);
	//EnQueue_LQ(Q, 23);
	//EnQueue_LQ(Q, 33);
	printf("length: %d\n",QueueLength_LQ(Q));
	GetHead_LQ(Q,t);
	printf("t: %d\n", t);
	DeQueue_LQ(Q, t);
	printf("t: %d\n", t);
	t=0;
	GetHead_LQ(Q,t);
	printf("t: %d\n", t);
	printf("null of notnull: %d\n",QueueEmpty_LQ(Q));
}
