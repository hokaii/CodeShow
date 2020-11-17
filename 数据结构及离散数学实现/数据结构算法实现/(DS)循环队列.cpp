#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef struct{
	int *elem;
	int front;
	int rear;
	int maxSize;
} SqQueue;

int InitQueue_Sq(SqQueue &Q, int size){
	Q.elem = (int*)malloc(size*sizeof(int));
	if(NULL == Q.elem)
		return OVERFLOW;
	Q.front = 0;
	Q.rear = 0;
	Q.maxSize = size;
	return OK;
}

bool QueueEmpty_Sq(SqQueue &Q){
	if(Q.front == Q.rear)
		return true;
	else
		return false;
}

int QueueLength_Sq(SqQueue &Q){
	int i= (Q.rear-Q.front+Q.maxSize)%Q.maxSize;
	return i;
}

int GetHead_Sq(SqQueue &Q, int &e){
	if(QueueEmpty_Sq)
		return ERROR;
	else{
		e = Q.elem[Q.front];
		Q.front = (Q.front+1) %Q.maxSize;
		return OK;
	}
}

int EnQueue_Sq(SqQueue &Q, int e){
	if(QueueLength_Sq(Q) == Q.maxSize-1){
		printf("队列已满！！");
		return ERROR;
	}
	else{
		int i = Q.rear;
		Q.elem[i] = e;
		Q.rear=(Q.rear+1)%Q.maxSize;
		return OK;
	}
}

int main(){
	SqQueue Q;
	printf("%d\n",InitQueue_Sq(Q, 6));
	printf("队列长度: %d\n",QueueLength_Sq(Q));
	int e=1;
	printf("%d\n",EnQueue_Sq(Q, e));
	printf("队列长度: %d\n",QueueLength_Sq(Q));
	EnQueue_Sq(Q, e);
	printf("队列长度: %d\n",QueueLength_Sq(Q));
	EnQueue_Sq(Q, e);
	printf("队列长度: %d\n",QueueLength_Sq(Q));
	EnQueue_Sq(Q, e);
	printf("队列长度: %d\n",QueueLength_Sq(Q));
	EnQueue_Sq(Q, e);
	printf("队列长度: %d\n",QueueLength_Sq(Q));
}
