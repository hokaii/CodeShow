#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef struct DuLNode{
	int data;
	struct DuLNode *prior,*next;
} DuLNode, *DuLinkList;

int InitList_DuL(DuLinkList &L){
	L = (DuLNode*)malloc(sizeof(DuLNode));
	if(L == NULL){
		printf("OVERFLOW");
		return ERROR;
	}
	L->next = L->prior = NULL;
	return OK;
}

bool ListEmpty_DuL(DuLinkList L){
	if(L->next == NULL)
		return true;
	else
		return false;
}

int ListLength_DuL(DuLinkList L){
	int temp;
	DuLNode *t = L->next;
	if(ListEmpty_DuL(L))
		return 0;
	while(t != NULL){
		t = t->next;
		temp++;
	}
	return temp;
}

DuLNode * Search_DuL(DuLinkList L, int e){
	DuLNode *s1 = L->next;
	while(s1 != NULL){
		if(s1->data == e){
			return s1;
		}
		s1 = s1->next;
	}	
	return NULL;
}

DuLNode * PriorElem_DuL(DuLNode *p){
	if(p->prior == NULL || p==NULL)
		return NULL;
	return p->prior;
}

DuLNode * NextElem_DuL(DuLNode *p){
	if(p->next==NULL || p==NULL)
		return NULL;
	return p->next;
}

DuLNode * MakeNode_DuL(int e){
	DuLNode *m1;
	m1 = (DuLNode*)malloc(sizeof(DuLNode));
	if(m1 == NULL)
		return NULL;
	m1->prior = NULL;
	m1->next = NULL;
	m1->data = e;
	return m1;
}

int InsertBefore_DuL(DuLNode *p, DuLNode*q){
	if(p->prior == NULL || p ==NULL || q == NULL)
		return ERROR;
	q->next = p;
	q->prior = p->prior;
	q->prior->next = q;
	p->prior = q;
}

int InsertAfter_DuL(DuLNode *p, DuLNode *q){
	if(p == NULL || q == NULL)
		return ERROR;
	if(p->next == NULL){
		q->prior = p;
		p->next = q;
		return OK;
	}
	q->next = p->next;
	q->prior = p;
	q->next->prior = q;
	p->next = q;
	return OK;
}

int Delete_DuL(DuLNode *p, int &e){
	if(NULL == p || NULL == p->prior)
		return ERROR;
	if(p->next != NULL){
		p->next->prior = p->prior;
	}
	e = p->data;
	p->prior->next = p->next;
	free(p);
	return OK;
}

void ListTraverse_DuL(DuLinkList L, void (*visit)(DuLNode *e)){
	DuLNode *lt = L->next;
	while(lt != NULL){
		visit(lt);
		lt = lt->next;
	}
}

void visit(DuLNode *e){
	printf("visit: %d, data is %d\n", e, e->data);
}

int main(){
	DuLinkList DL;
	InitList_DuL(DL);
	DuLNode *p1 = MakeNode_DuL(10);
	DuLNode *p2 = MakeNode_DuL(12);
	DuLNode *p3 = MakeNode_DuL(14);
	InsertAfter_DuL(DL, p1);
	InsertAfter_DuL(p1, p3);
	InsertBefore_DuL(p3, p2);
	printf("DL->prior: %d,DL: %d,DL->next: %d\n",DL->prior, DL, DL->next);
	printf("p1->prior: %d,p1: %d,p1->next: %d\n",p1->prior, p1, p1->next);
	printf("p2->prior: %d,p2: %d,p2->next: %d\n",p2->prior, p2, p2->next);
	printf("p3->prior: %d,p3: %d,p3->next: %d\n",p3->prior, p3, p3->next);
	if(!ListEmpty_DuL(DL))
		printf("list length is: %d\n",ListLength_DuL(DL));
	ListTraverse_DuL(DL, visit);
	int t1;
	Delete_DuL(p1, t1);
	printf("t1: %d\n", t1);
	printf("DL->prior: %d,DL: %d,DL->next: %d\n",DL->prior, DL, DL->next);
	printf("p1->prior: %d,p1: %d,p1->next: %d\n",p1->prior, p1, p1->next);
	printf("p2->prior: %d,p2: %d,p2->next: %d\n",p2->prior, p2, p2->next);
	printf("p3->prior: %d,p3: %d,p3->next: %d\n",p3->prior, p3, p3->next);
	if(!ListEmpty_DuL(DL))
		printf("list length is: %d\n",ListLength_DuL(DL));
	ListTraverse_DuL(DL, visit);
	printf("search elem: %d\n",Search_DuL(DL, 12));
	printf("Prior Elem: %d\n",PriorElem_DuL(p2));
	printf("Next Elem: %d\n",NextElem_DuL(p2));
}
