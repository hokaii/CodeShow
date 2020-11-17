#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define LH +1 //左子树比右子树高,简称左高 
#define EH 0 //左、右子等高, 简称等高 
#define RH -1 //右子树比左子树高，简称右高 

typedef struct BBSTNode{ 
	RcdType data;
	int bf;
	struct BBSTNode *lchild,*rchild;
} *BBSTree;

void R_Rotate(BBSTree &p){
	//LL型,对最小失衡子树右旋调整 
	BBSTree lc = p->lchild;
	p->lchild = lc->rchild;
	lc->rchild = p;
	p = lc;
}

void L_Rotate(BBSTree &p){
	//RR型,对最小失衡子树左旋调整
	BBSTree rc = p->rchild;
	p->rchild = rc->lchild;
	rc->lchild = p;
	p = rc; 
}

void LR_Rotate(BBSTree &p){
	//LR型,先左旋使子树成为LL型,再右旋调整
	L_Rotate(p->lchild);
	R_Rotate(p); 
}

void RL_Rotate(BBSTree &p){
	//RL型,先右旋使子树成为RR型,再左旋调整
	R_Rotate(p->rchild);
	L_Rotate(p); 
}

void LeftBalance(BBSTree &T){
	//实现对树T的左平衡处理
	BBSTree lc, rd;
	lc = T->lchild;
	switch(lc->bf){
		case LH:
			T->bf = lc->bf = EH;
			R_Rotate(T);
			break;
		case RH:
			rd = lc->rchild;
			switch(rd->bf){
				case LH:
					T->bf = RH;
					lc->bf = EH;
					break;
				case EH:
					T->bf = lc->bf = EH;
					break;
				case RH:
					T->bf = EH;
					lc->bf = LH;
					break;
			}
			rd->bf = EH;
			L_Rotate(T->lchild);//先对T的子树左旋调整 
			R_Rotate(T);//对T作右旋调整 
			break;
	} 
}

void RightBalance(BBSTree &T){
	//实现对树T的右平衡处理
	BBSTree rc, ld;
	rc = T->rchild;
	switch(rc->bf){
		case LH:
			ld = rc->lchild;
			switch(ld->bf){
				case LH:
					T->bf = EH;
					rc->bf = RH;
					break;
				case EH:
					T->bf = rc->bf = EH;
					break;
				case RH:
					T->bf = LH;
					rc->bf = EH;
					break;
			}
			ld->bf = EH;
			R_Rotate(T->rchild);//先对T的子树右旋调整 
			L_Rotate(T);//对T作左旋调整 
			break;
		case RH:
			T->bf = rc->bf = EH;
			L_Rotate(T);
			break;
	} 
}

int InsertAVL(BBSTree &T, RcdType e, int &taller){
	//实现对e插入到二叉树的操作
	if(NULL == T){
		T = (BSTree)malloc(sizeof(BSTNode));
		T->data = e;
		T->bf = EH;
		T->lchild = NULL;
		T->rchild = NULL;
		taller = OK;
	} 
	else if(e.key == T->data.key){
		taller = ERROR;
		return FALSE;
	}
	else if(e.key < T->data.key){
		if(ERROR == InsertAVL(T->lchild, e, taller))
			return ERROR;
		if(OK == taller){
			switch(T->bf){
				case LH: 
					LeftBalance(T);
					taller = ERROR;
					break;
				case EH:
					T->bf = LH;
					taller = OK;
					break;
				case RH:
					T->bf = EH;
					taller = ERROR;
					break;
			}
		}
	}
	else{
		if(ERROR == InsertAVL(T->rchild, e, taller))
			return ERROR;
		if(OK == taller){
			switch(T->bf){
				case LH:
					T->bf = EH;
					taller = ERROR;
					break;
				case EH:
					T->bf = RH;
					taller = OK;
					break;
				case RH:
					RightBalance(T);
					taller = ERROR;
					break;
			}
		}
	}
	return OK;
}
