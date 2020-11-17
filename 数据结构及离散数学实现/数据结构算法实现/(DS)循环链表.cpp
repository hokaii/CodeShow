#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef struct LNode{
	int data;
	struct LNode *next;
} LinkList, *CirLinkList;

int InitList_CL(CirLinkList &L){
	L = (LNode*)malloc(sizeof(LNode));
	if(L == NULL)
		return ERROR;
	L->next = L;
	return OK;
}

int DeleteAfter_CL(CirLinkList L, LNode *p, int &e){//É¾³ýºó¼Ì 
	LNode * q;
	if(L == L->next)
		return ERROR;
	if(p->next == L)
		p = L;
	q = p->next;
	p->next = q->next;
	e = q->data;
	printf("%d",e);
	free(q);
	return OK;
}

void Split(CirLinkList &LO, CirLinkList &LC, CirLinkList &LL){//·Ö²ð 
	char  ch;
	CirLinkList po, pc, pl;
	po = LO->next;
	LC = LO;
	InitList_CL(LL);
	pc = LC;
	pl = LL;
	while(po != LO){
		ch = po->data;
		if(ch >= 'A' && ch <= 'Z'){
			pc->next = po;
			pc = po;
		}
		else{
			pl->next = po;
			pl = po;
		}
		po = po->next;
	}
	pc->next = LC;
	pl->next = LL;
}

void josephus(CirLinkList L, int n, int m){
	int i=0, j;
	LNode *p=L;
	while(1){
		if(p == L)
			p = L->next;
		if(p->next == L)
			p = L;
		if(i == 3){
			i = -1;
			if(DeleteAfter_CL(L, p, j) == ERROR)
				break;
		}
		p = p->next;
		i++;
	}
}

void InsertAfter(CirLinkList L, int n){
	LNode *p;
	p = (LNode*)malloc(sizeof(LNode));
	p->data = n;
	p->next = L->next;
	if(!L->next)
		L = p;
	else
		L->next = p;
}

int main(){
	CirLinkList L1;
	InitList_CL(L1);
	for(int i=9; i>0; i--)
		InsertAfter(L1, i);
	josephus(L1, 9, 5);
}
