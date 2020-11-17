#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef int KeyType;
typedef int RcdType;
typedef struct BSTNode{
	RcdType data;
	struct BSTNode *lchild, *rchild;
} BSTNode, *BSTree;

int InitBST(BSTree &T){
	//构造一颗空的二叉查找树T 
	T = (BSTree)malloc(sizeof(BSTNode));
	return OK;
}

BSTree SearchBST(BSTree T, KeyType key){
	//若二叉查找树T中存在值为key的结点, 则返回改结点指针, 否则返回NULL 
	if(T == NULL)
		return NULL;
	if(T->data == key)
		return T;
	if(T->data > key)
		return SearchBST(T->lchild, key);
	return SearchBST(T->rchild, key);
}

BSTree SearchBST_I(BSTree T, KeyType key){
	//上述查找算法的非递归实现
	while(T!=NULL){
		if(T->data == key)
			return T;
		else if(T->data > key)
			T = T->lchild;
		else
			T = T->rchild;
	} 
	return NULL;
}

int InsertBST(BSTree &T, RcdType e){
	//若二叉查找树T中不存在值为e.key的结点, 则插入到T
	if(T == NULL){
		BSTNode *s;
		s = (BSTNode*)malloc(sizeof(BSTNode));
		s->data = e;
		s->lchild = s->rchild = NULL;
		T = s;
		return OK;
	}
	if(e < T->data)
		return InsertBST(T->lchild, e);
	if(e > T->data)
		return InsertBST(T->rchild, e);
	return ERROR;//e == T->data,结点存在 
}

int DeleteBST(BSTree &T, KeyType key){
	//若二叉查找树T中存在值为key的结点,则删除该结点,并返回OK, 否则返回ERROR 
	int DeleteNode(BSTree &p);
	if(T == NULL)
		return ERROR;
	if(T->data == key){
		DeleteNode(T);
		return OK;
	}
	else if(key < T->data)
		return DeleteBST(T->lchild, key);
	return DeleteBST(T->rchild, key);
}

int DeleteNode(BSTree &p){
	if(NULL == p->rchild){
		p = p->lchild;
		return OK;
	}
	else if(NULL == p->rchild){
		p = p->rchild;
		return OK;
	}
	else{
		p->data = p->rchild->data;
		DeleteNode(p->rchild);
		return OK;
	}
}

/*
void DeleteNode(BSTree &p){
	//删除二叉查找树中的p结点,引用形参p的实参是要删除的p结点的双亲指向其指针域
	BSTNode *q, *s;
	q = p;
	if(NULL == p->rchild) {
		p = p->lchild;
		free(p);
	}
	else if(NULL == p->lchild){
		p = p->rchild;
		free(p);
	}
	else{
		
	}
}
*/
int main(){
	BSTree T = NULL;
	int A[9] = {5, 2, 7, 1, 4, 6, 8, 3, 9};
	for(int i=0;i<9;i++)
		InsertBST(T, A[i]);
	DeleteBST(T, 5);
	printf("%d", T->data);
} 
