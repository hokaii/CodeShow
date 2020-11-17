#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1
#define LH +1 //����������������,������ 
#define EH 0 //�����ӵȸ�, ��Ƶȸ� 
#define RH -1 //���������������ߣ�����Ҹ� 

typedef struct BBSTNode{ 
	RcdType data;
	int bf;
	struct BBSTNode *lchild,*rchild;
} *BBSTree;

void R_Rotate(BBSTree &p){
	//LL��,����Сʧ�������������� 
	BBSTree lc = p->lchild;
	p->lchild = lc->rchild;
	lc->rchild = p;
	p = lc;
}

void L_Rotate(BBSTree &p){
	//RR��,����Сʧ��������������
	BBSTree rc = p->rchild;
	p->rchild = rc->lchild;
	rc->lchild = p;
	p = rc; 
}

void LR_Rotate(BBSTree &p){
	//LR��,������ʹ������ΪLL��,����������
	L_Rotate(p->lchild);
	R_Rotate(p); 
}

void RL_Rotate(BBSTree &p){
	//RL��,������ʹ������ΪRR��,����������
	R_Rotate(p->rchild);
	L_Rotate(p); 
}

void LeftBalance(BBSTree &T){
	//ʵ�ֶ���T����ƽ�⴦��
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
			L_Rotate(T->lchild);//�ȶ�T�������������� 
			R_Rotate(T);//��T���������� 
			break;
	} 
}

void RightBalance(BBSTree &T){
	//ʵ�ֶ���T����ƽ�⴦��
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
			R_Rotate(T->rchild);//�ȶ�T�������������� 
			L_Rotate(T);//��T���������� 
			break;
		case RH:
			T->bf = rc->bf = EH;
			L_Rotate(T);
			break;
	} 
}

int InsertAVL(BBSTree &T, RcdType e, int &taller){
	//ʵ�ֶ�e���뵽�������Ĳ���
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
