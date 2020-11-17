#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
typedef struct {
	int *elem;
	int top;
	int size;
	int increment;
} SqStack;

int InitStack_Sq(SqStack &S, int size, int inc){//��ʼ�� 
	S.elem = (int*)malloc(size*sizeof(int));
	if(NULL == S.elem)
		return -1;
	S.top = 0;
	S.size = size;
	S.increment = inc;
	return 1;
}

bool StackEmpty_Sq(SqStack &S){//�ж��Ƿ�Ϊ�� 
	if(S.top>0)
		return false;
	else
		return true;
}

void ClearStack_Sq(SqStack &S){//���ջ 
	for(int i = 0; i<S.top;i++){
		S.elem[i] = NULL;
	}
	S.top = 0;
}

int Push_Sq(SqStack &S, int e){//��Ԫ��ѹ��ջ 
	int *newbase;
	if(S.top >= S.size){
		newbase = (int*)realloc(S.elem, (S.size+S.increment) * sizeof(int));
		if(NULL == newbase)
			return -1;
		S.elem = newbase;
		S.size += S.increment;
	}
	S.elem[S.top++] = e;
	return 1;
}

int Pop_Sq(SqStack &S,int &e){//ջ��Ԫ�س�ջ 
	if(S.top > 0){
		e = S.elem[S.top-1];
		S.elem[S.top-1] = NULL;
		S.top--;
	}
	else
		e = NULL;
}

int GetTop_Sq(SqStack S, int &e){//ȡջ��Ԫ�� 
	if(S.top > 0){
		e = S.elem[S.top-1];
	}
	else
		e = NULL;
}

void Converstion(SqStack S, int n){//ʮ����ת�˽��� 
	while(n!=0){
		Push_Sq(S, n%8);
		n = n / 8;
	}
	while(!StackEmpty_Sq(S)){
		Pop_Sq(S, n);
		printf("%d", n);
	}
	printf("\n");
}

int Matching(SqStack S, int *a, int n){//������Ϊ1��������Ϊ2�� �������Ϊ3�� �Ҵ�����Ϊ4 
	int i = 0;
	int temp;
	while(i < n){
		switch(a[i]){
			case 1:
			case 3:Push_Sq(S, a[i]); i++; break;
			case 2:Pop_Sq(S, temp);
					 if(temp != 1)
					 	return ERROR;
					 else
					 	i++;
					break;
			case 4:Pop_Sq(S, temp);
					 if(temp != 3)
					 	return ERROR;
					 else
					 	i++;
					break;
			default: i++;
		}
	}
	if(StackEmpty_Sq(S))
		return OK;
	else
		return ERROR;
} 

int main(){
	SqStack S;
	printf("-------test-------\n");
	int e;
	InitStack_Sq(S, 10, 5);
	Push_Sq(S, 14);
	printf("%d\n",StackEmpty_Sq(S));
	Pop_Sq(S, e);
	printf("%d\n", e);
	Push_Sq(S, 20);
	Pop_Sq(S, e);
	printf("%d\n",e);
	ClearStack_Sq(S);
	Pop_Sq(S, e);
	printf("%d\n", e);
	printf("%d\n", StackEmpty_Sq(S));
	printf("-------test-------\n");
	
	e = 1348;
	Converstion(S, e);
	
	int a[7] = {3,1,1,6,2,2,4};
	printf("%d",Matching(S, a, 7));
}
