#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef char AtomType;
typedef enum{
	ATOM, LIST//ATOM值为0表示原子, LIST值为1表示表结点 
} ElemTag;
typedef struct GLNode {
	ElemTag tag;//区分原子结点和表结点 
	union{//原子结点和表结点共用存储空间 
		AtomType atom;//当tag==ATOM时,本项有意义,存放原子结点值 
		struct{//当tag==LIST时,本项有意义 
			struct GLNode *hp;
			struct GLNode *tp;
		} ptr;//表结点的指针域,其中ptr.hp指向表头,ptr.tp指向表尾 
	} un;
} GLNode, *GList;//广义表

GLNode *MakeAtom(AtomType e){
	GLNode *n;
	n = (GLNode*)malloc(sizeof(GLNode));
	n->tag = ATOM;
	n->un.atom = e;
	return n;
}

void InitGList(GList &L){//初始化为一个嵌套两层的广义表 
	L = (GList)malloc(sizeof(GLNode));
	L->tag = LIST;
	L->un.ptr.hp = NULL;
	L->un.ptr.tp = NULL; 
}

GLNode *GetHead(GList L){
	if(L->un.ptr.hp != NULL)
		return L->un.ptr.hp;
	return NULL;
}

GList GetTail(GList L){
	if(L->un.ptr.tp != NULL)
		return L->un.ptr.tp;
	return NULL;
}

int InsertHead(GList &L, GLNode *p){
	bool GListEmpty(GList L);
	GLNode *p1;
	GList Lp1;
	Lp1 = (GList)malloc(sizeof(GLNode));
	Lp1->tag = LIST;
	Lp1->un.ptr.hp = p;
	Lp1->un.ptr.tp = L->un.ptr.hp;
	if(GListEmpty(L)){
		L = Lp1;
		return OK;
	}
	L->un.ptr.hp = Lp1;
	return OK;
}

int Append(GList &L, GLNode *p){
	bool GListEmpty(GList L);
	//在广义表L的末尾添加新的表结点, 并将参数p赋予其表头指针hp
	GLNode *pp;
	GList tail;
	tail = (GList)malloc(sizeof(GLNode));
	if(NULL==tail)
		return OVERFLOW;
	tail->tag = LIST;
	tail->un.ptr.hp = p;
	tail->un.ptr.tp = NULL;
	if(GListEmpty(L))
		L->un.ptr.hp = p;
	else{
		for(pp = L; pp->un.ptr.tp!=NULL; pp=pp->un.ptr.tp);//定位到最后一个结点
			pp->un.ptr.tp = tail;
	}
	return OK;
}

int Append_List(GList &L, GList LP){
	bool GListEmpty(GList L);
	GLNode *pp;
	if(GListEmpty(L)){
		L->un.ptr.hp = LP;
		return OK;
	}
	for(pp = L; pp->un.ptr.tp!=NULL; pp=pp->un.ptr.tp)//定位到最后一个结点
		pp->un.ptr.tp = LP;
	return OK;
}

int DeleteHead(GList L, GList &p){
	if(L->un.ptr.hp == NULL)
		return ERROR;
	p = L->un.ptr.hp;
	L->un.ptr.hp = p->un.ptr.tp;
	return OK;
}

int GListDepth_one(GList L){//方式一分解为表头表尾求深度 
	bool GListEmpty(GList L);
	int h1,h2;
	//if(L == NULL)
		//return 0;
	if(GListEmpty(L))
		return 1;
	if(ATOM == L->tag)
		return 0;
	h1 = GListDepth_one(L->un.ptr.hp)+1;
	h2 = GListDepth_one(L->un.ptr.tp);
	return h1>=h2?h1 : h2;
}

int GListDepth_two(GList L){//方式二分解为各个元素求深度 
	bool GListEmpty(GList L);
	GLNode *p = L;
	int num,t;
	if(L == NULL)
		return 0;
	if(GListEmpty(L))
		return 1;
	else if(ATOM == p->tag)
		return 0;
	else
		num++;
	if(p->un.ptr.tp != NULL)
		return num>(GListDepth_two((p->un.ptr.tp)->un.ptr.hp)+1)? num:(GListDepth_two((p->un.ptr.tp)->un.ptr.hp)+1);
	else 
		return num>(GListDepth_two(p->un.ptr.hp) + 1)? num:(GListDepth_two(p->un.ptr.hp) + 1);
}

void CopyGList(GList L, GList &CopyL){
	if(L){
		if(L->tag == ATOM){
			CopyL->tag = ATOM;
			CopyL->un.atom = L->un.atom;
		}
		else{
			CopyL->tag = LIST;
			if(L->un.ptr.hp)
				CopyGList(L->un.ptr.hp, CopyL->un.ptr.hp);
			else
				CopyL->un.ptr.hp = NULL;
		}
		if(L->un.ptr.tp)
			CopyGList(L->un.ptr.tp, CopyL->un.ptr.tp);
		else
			CopyL->un.ptr.tp = NULL;
	}
}

int GListLength(GList L){
	GLNode *p = L/*->un.ptr.hp*/;
	int num;
	while(p!=NULL){
		num++;
		p = p->un.ptr.tp;
	}
	return num;
}

bool GListEmpty(GList L){
	if(L == NULL){
		//printf("广义表不存在!\n");
		return true; 
	}
	if(L->tag == LIST && !L->un.ptr.hp && !L->un.ptr.tp)
		return true;
	return false;
}

void GListTraverse(GList L, void (*visit)(AtomType e)){
	GLNode *p = L;
	if(p){
		if(p->tag == ATOM)
			visit(p->un.atom);
		else{
			GListTraverse(p->un.ptr.hp, visit);
			GListTraverse(p->un.ptr.tp, visit);
		}
	}
}

void visit(AtomType e){
	printf("traverse to: %c\n", e);
}

int main(){
	GList L1,L2,L3,L4;/*
	GLNode *p;
	p=(GLNode*)malloc(sizeof(GLNode));
	p->tag = ATOM;
	p->un.atom = 'a';*/
	InitGList(L1);
	InitGList(L2);
	InitGList(L3);
	Append_List(L1, L2);
	Append_List(L2, L3);
	Append(L1, MakeAtom('a'));
	Append(L1, MakeAtom('b'));
	Append(L2, MakeAtom('c'));
	Append(L3, MakeAtom('d'));
	printf("L1:%d, hp:%d, tp:%d\n",L1, L1->un.ptr.hp, L1->un.ptr.tp);
	printf("L2:%d, hp:%d, tp:%d\n",L2, L2->un.ptr.hp, L2->un.ptr.tp);
	printf("L3:%d, hp:%d, tp:%d\n",L3, L3->un.ptr.hp, L3->un.ptr.tp);
	printf("list length: %d\n", GListLength(L1));
	printf("list length: %d\n", GListLength(L2));
	printf("list length: %d\n", GListLength(L3));
	printf("L1 empty or not: %d\n",GListEmpty(L1));
	printf("list depth 1: %d\n",GListDepth_one(L1));
	printf("list depth 2: %d\n",GListDepth_two(L1));
	GListTraverse(L1, visit);
} 
