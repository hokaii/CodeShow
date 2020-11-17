#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define MAXSIZE 100

typedef char TElemType;
typedef struct BiTNode {
	TElemType data;
	struct BiTNode *lchild,*rchild;
} BiTNode, *BiTree;//二叉链表

//链栈定义
typedef struct LSNode{
	BiTree data;//数据域 
	struct LSNode * next;//指针域 
}LSNode, *LStack;//结点和链栈类型

void InitStack_LS(LStack &S){
	S = (LStack)malloc(sizeof(LSNode));
	S -> next = NULL;
}

bool StackEmpty_LS(LStack S){
	if(NULL == S->next)
		return true;
	else
		return false;
}

int Push_LS(LStack &S, BiTree e){
	LSNode *t;
	t = (LSNode*)malloc(sizeof(LSNode));
	if(NULL == t)
		printf("OVERFLOW");
	t->data = e;
	t->next = S; 
	S = t;
	return OK;
}

int Pop_LS(LStack &S, BiTree &e){
	LSNode *t;
	if(NULL == S)
		return ERROR;
	t = S;
	e = S->data;
	S = S->next;
	free(t);
	return OK;
}

int GetTop_LS(LStack S, BiTree &e){
	e = S->data;
	return OK;
}
//链栈定义结束 

//链队列定义
typedef struct LQNode{
	BiTree data;
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

bool QueueEmpty_LQ(LQueue Q){
	if(Q.front == NULL)
		return true;
	else
		return false;
}

int DeQueue_LQ(LQueue &Q, BiTree &e){
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

int EnQueue_LQ(LQueue &Q, BiTree e){
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
//链队列定义结束 

void InitBiTree(BiTree &T){
	//创建一颗空二叉树 
	T = (BiTree)malloc(sizeof(BiTNode));
	T->data = NULL;
	T->lchild = NULL;
	T->rchild = NULL;
} 

BiTree MakeBiTree(TElemType e, BiTree L, BiTree R){
	//创建一颗二叉树T,其中根节点为e,L和R分别为左右子书 
	BiTree T;
	T = (BiTree)malloc(sizeof(BiTNode));
	T->rchild = R;
	T->lchild = L;
	T->data = e;
	return T;
}

bool BiTreeEmpty(BiTree T){
	//判断二叉树是否为空 
	if(T == NULL)
		return true;
	if(!T->data && !T->lchild && !T->rchild)
		return true;
	return false;
}

int BreakBiTree(BiTree &T, BiTree &L, BiTree &R){
	//将二叉树分解成跟、左子树、右子树三个部分 
	L = T->lchild;
	R = T->rchild;
	T->lchild = NULL;
	T->rchild = NULL;
	return OK;
}

int ReplaceLeft(BiTree &T, BiTree &LT){
	//替换左子树 
	bool BiTreeEmpty(BiTree T);
	if(!BiTreeEmpty(T)){
		BiTree TT;
		TT = T->lchild;
		T->lchild = LT;
		LT = TT;
		return OK;
	}
	return ERROR;
}

int ReplaceRight(BiTree &T, BiTree &RT){
	//替换右子树 
	bool BiTreeEmpty(BiTree T);
	if(!BiTreeEmpty(T)){
		BiTree TT;
		TT = T->rchild;
		T->rchild = RT;
		RT = TT;
		return OK;
	}
	return ERROR;
}

int PreOrderTraverse(BiTree T, int (*visit)(TElemType e)){
	//先序递归遍历二叉树T. 
	if(T){
		visit(T->data);
		PreOrderTraverse(T->lchild, visit);
		PreOrderTraverse(T->rchild, visit);
	}
}

int InOrderTraverse(BiTree T, int (*visit)(TElemType e)){
	//中序递归遍历二叉树T. 
	if(BiTreeEmpty(T))
		return OK;
	InOrderTraverse(T->lchild, visit);
	visit(T->data);
	return InOrderTraverse(T->rchild, visit);
}

int visit(TElemType e){
	printf("visit: %c\n", e);
	return ERROR;
}

BiTNode *GoFarLeft(BiTree T, LStack &S){
	//从T结点出发,沿左分支走到底,沿途结点的指针入栈S,返回左下结点的指针
	if(BiTreeEmpty(T))
		return NULL;
	while(!BiTreeEmpty(T->lchild)){
		Push_LS(S, T);
		T = T->lchild;
	}
	return T;
}

void InorderTraverse_I(BiTree T, int (*visit)(TElemType e)){
	//中序非递归遍历 
	BiTree t;
	LStack S;
	InitStack_LS(S);
	t = GoFarLeft(T, S);
	while(!BiTreeEmpty(t)){
		visit(t->data);
		if(!BiTreeEmpty(t->rchild))  
			t = GoFarLeft(t->rchild, S);
		else if(!StackEmpty_LS(S))
			Pop_LS(S, t);
		else
			t = NULL;
	}
}

/*
void PostOrder(BiTree T, int (*visit)(TElemType e)){
	//后序非递归遍历
	BiTree p=T,r;
	LStack S;
	InitStack_LS(S);
	while(p || !StackEmpty_LS(S)){
		if(p){
			Push_LS(S, p);
			p = p->lchild;
		}
		else{
			GetTop_LS(S, p);
			if(p->rchild==NULL){
				Pop_LS(S, p);
				visit(p->data);
				GetTop_LS(S, r);
				if(r && r->rchild !=p)
					p=r->rchild;
				else
					p=r;
			}
			else
				p=p->rchild;
		}
	}
}*/

void LevelOrderTraverse(BiTree T, int (*visit)(TElemType e)){
	//层次遍历二叉树T
	if(!BiTreeEmpty(T)) {
		LQueue Q;
		InitQueue_LQ(Q);
		BiTree p = T;
		visit(p->data);
		EnQueue_LQ(Q, p);
		while(DeQueue_LQ(Q, p)){
			if(!BiTreeEmpty(p->lchild)){
				visit(p->lchild->data);
				EnQueue_LQ(Q, p->lchild);
			}
			if(!BiTreeEmpty(p->rchild)){
				visit(p->rchild->data);
				EnQueue_LQ(Q, p->rchild);
			}
		}
	}
} 

/*
三叉链表的先序非递归遍历
int PreOrderTraverse(TriTree T, int (*visit)(TElemType e)){
	//先序非递归遍历二叉树T，visit的实参是对数据元素操作的应用函数
	TriTree p, pr;
	if(T != NULL){
		p = T;
		while(p != NULL){
			visit(p->data);
			if(p->lchild != NULL)
				p = p->lchild;//若有左孩子, 继续访问 
			else if(p->rchild != NULL)
				p = p->rchild;//若有右孩子, 继续访问 
			else{//沿双亲指针链查找, 找到第一个有右孩子的p结点, 找不到则结束 
				do{
					pr = p;
					p = p->parent;
				}while(p != NULL && (p->rchild == pr || NULL == p->rchild));
				if(p != NULL)
					p = p->rchild;//找到后, p指向右孩子结点 
			}
		}
	} 
*/

void DestroyBiTree(BiTree &T){
	//销毁二叉树
	if(!BiTreeEmpty(T)) {
		DestroyBiTree(T->lchild);
		DestroyBiTree(T->rchild);
		free(T);
	}
}

int BiTreeDepth(BiTree T){
	//求二叉树深度 
	int DepthLeft, DepthRight;
	if(BiTreeEmpty(T))
		return 0;
	DepthLeft = BiTreeDepth(T->lchild);
	DepthRight = BiTreeDepth(T->rchild);
	return 1+(DepthLeft>DepthRight?DepthLeft:DepthRight);
}

void CountLeaf(BiTree T, int &count){
	//求二叉树叶子结点个数
	if(!BiTreeEmpty(T)){
		if(BiTreeEmpty(T->lchild) && BiTreeEmpty(T->rchild))
			count++;
		CountLeaf(T->lchild, count);
		CountLeaf(T->rchild, count);
	}
}

BiTree CreateBiTree(char *defBT, int &i){
	//基于先序遍历框架构造二叉树,defBT为树形描述序列,i为defBT的当前位标,初值为0
	BiTree T;
	char ch;
	LStack S;
	ch = defBT[i++];
	if(ch == '#')
		InitStack_LS(S);
	else{
		T = MakeBiTree(ch, NULL, NULL);
		T->lchild = CreateBiTree(defBT, i);
		T->rchild = CreateBiTree(defBT, i);
	}
	return T;
}

int GetWide(BiTree T){
	BiTree Q[MAXSIZE];
	BiTree p;
	int maxwide=0,wide=0;
	int front=-1, rear=-1;
	int last=0;
	Q[++rear]=T;
	while(front<rear){
		wide++;
		p=Q[++front];
		if(p->lchild)
			Q[++rear]=p->lchild;
		if(p->rchild)
			Q[++rear]=p->rchild;
		if(front==last){
			if(wide>maxwide)
				maxwide=wide;
			wide=0;
			last=rear;
		}
	}
	return maxwide;
}

void LinkLeaf_PostOrder(BiTree T, BiTNode* &p){
	if(T){
		if(!T->lchild && !T->rchild){
			p->rchild = T;
			p = p->rchild;
		}
		LinkLeaf_PostOrder(T->lchild, p);
		LinkLeaf_PostOrder(T->rchild, p);
	}
}

void LinkLeaf(BiTree T, BiTNode* head){
	BiTNode *t = head;
	LinkLeaf_PostOrder(T, t);
}

bool Similar(BiTree T1, BiTree T2){
	//判断两棵树是否相似
	if((T1&&!T2)||(!T1&&T2))
		return 0;
	if(!(T1&&T2))
		return 1;
	return Similar(T1->lchild, T2->lchild)&&Similar(T1->rchild, T2->rchild);
}

int fchnsib_depth(BiTree t){
	//孩子兄弟链表求树深度
	if(!t)
		return 0;
	int fdepth = fchnsib_depth(t->lchild);
	int ndepth = fchnsib_depth(t->rchild);
	if(fdepth+1>ndepth)
		return fdepth+1;
	else
		return ndepth;
}

int GetLevel(BiTree T, BiTNode *q){
	if(!T)
		return 0;
	int front=-1, rear=-1;
	int last=0,level=1;
	BiTree Q[100];
	Q[++rear]=T;
	BiTree p;
	while(front<rear){
		p=Q[++front];
		if(p->lchild)
			Q[++rear] = p->lchild;
		if(p->rchild)
			Q[++rear] = p->rchild;
		if(p==q)
			return level;
		if(front==last){
			level++;
			last=rear;
		}
	}
	return 0;
} 

int main(){
	BiTree A1, B1, C1;
	BiTree D1 = MakeBiTree('z', NULL, NULL);
	int count;
	//B1 = MakeBiTree('B', MakeBiTree('D', MakeBiTree('H', NULL, NULL), MakeBiTree('I', NULL, NULL)), MakeBiTree('E', NULL, NULL));
	B1 = MakeBiTree('B', MakeBiTree('D', NULL, MakeBiTree('I', D1, NULL)), MakeBiTree('E', NULL, NULL));
	//A1 = MakeBiTree('A', B1, MakeBiTree('C', MakeBiTree('F', NULL, NULL), NULL));
	A1 = MakeBiTree('A', B1, NULL);
	C1 = MakeBiTree('a', MakeBiTree('b', MakeBiTree('d', MakeBiTree('h', NULL, NULL), MakeBiTree('i', NULL, NULL)), 
		 MakeBiTree('e', NULL, NULL)), MakeBiTree('c', MakeBiTree('F', NULL, NULL), NULL));
	
	printf("A: %d, A->lchild: %d, A->rchild: %d\n", A1, A1->lchild, A1->rchild);
	//printf("B: %c, B->lchild: %c, B->rchild: %c\n", B1->data, B1->lchild->data, B1->rchild->data);
	printf("中序遍历\n");
	//InOrderTraverse(A1, visit);
	InorderTraverse_I(A1, visit);
	printf("层次遍历\n");
	//DestroyBiTree(A1);
	LevelOrderTraverse(A1, visit);
	printf("先序遍历\n");
	PreOrderTraverse(A1, visit); 
	//PostOrder(A1, visit); 
	printf("A1 depth: %d\n",BiTreeDepth(A1));	
	CountLeaf(A1, count);
	printf("A1 leaf count: %d\n", count);
	printf("max wide: %d\n", GetWide(A1));
	
	LevelOrderTraverse(C1, visit);
	printf("%d", Similar(A1, B1));
	
	printf("%d", fchnsib_depth(A1));
	
	printf("%d", GetLevel(A1, D1));
}
