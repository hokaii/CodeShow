#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define OK 1
#define LH +1 //����������������,������ 
#define EH 0 //�����ӵȸ�, ��Ƶȸ� 
#define RH -1 //���������������ߣ�����Ҹ�

typedef struct BBSTNode{ 
	int data;
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

void LeftBalance(BBSTree &T){
	//ʵ�ֶ���T����ƽ�⴦��
	BBSTree lc, rd;
	lc = T->lchild;
	switch(lc->bf){
		case LH://��� 
			T->bf = lc->bf = EH;
			R_Rotate(T);
			break;
		case RH://�Ҹ� 
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

int InsertAVL(BBSTree &T, int e, int &taller){
	//ʵ�ֶ�e���뵽�������Ĳ���
	if(NULL == T){
		T = (BBSTree)malloc(sizeof(BBSTNode));
		T->data = e;
		T->bf = EH;
		T->lchild = NULL;
		T->rchild = NULL;
		taller = TRUE;
	} 
	else if(e == T->data){
		taller = FALSE;
		return FALSE;
	}
	else if(e < T->data){
		if(FALSE == InsertAVL(T->lchild, e, taller))
			return FALSE;
		if(taller==TRUE){
			switch(T->bf){
				case LH: 
					LeftBalance(T);
					taller = FALSE;
					break;
				case EH:
					T->bf = LH;
					taller = TRUE;
					break;
				case RH:
					T->bf = EH;
					taller = FALSE;
					break;
			}
		}
	}
	else{
		if(FALSE == InsertAVL(T->rchild, e, taller))
			return FALSE;
		if(taller == TRUE){
			switch(T->bf){
				case LH:
					T->bf = EH;
					taller = FALSE;
					break;
				case EH:
					T->bf = RH;
					taller = TRUE;
					break;
				case RH:
					RightBalance(T);
					taller = FALSE;
					break;
			}
		}
	}
	return TRUE;
}

int DeleteAVL(BBSTree &T, int e, BBSTree f, BBSTree p, int &taller, int mark){
	//pָ��ǰ��㣬fָ��p�ĸ���㣬��ʼ��Ϊ�գ�*taller��ʼ��ΪFALSE��mark����f��p�Ĺ�ϵ����ʼ��Ϊ0 
	BBSTree r;
	int tmp;
	if(!p)
		return ERROR;
	else{		
		if(e < p->data){//��Ѱ������	
			if(!DeleteAVL(T, e, p, p->lchild, taller, 0))
				return ERROR;
			if(taller){
				switch(p->bf){
					case EH:
						p->bf = RH;
						taller = FALSE;
						break;
					case RH:
						if(!f)
							RightBalance(T);
						else
							RightBalance(f->lchild);
						taller = TRUE;
						break;
					case LH:
						p->bf = EH;
						taller = TRUE;
						break;				
				}			
			}
		}			
		else if(e > p->data){	//��Ѱ������
			if(!DeleteAVL(T, e, p, p->rchild, taller, 1))
				return ERROR;	
			if(taller){
				switch(p->bf){
					case LH:
						if(!f)
							LeftBalance(T);
						else
							LeftBalance(f->rchild);
						taller = TRUE;
						break;
					case EH:
						p->bf = LH;
						taller = FALSE;
						break;
					case RH:
						p->bf = EH;
						taller = TRUE;
						break;				
				}
			}
		}
		else{			
			if(p->lchild!=NULL && p->rchild==NULL){//ֻ��������
				if(!f)//����� 
					T = p->lchild;			
				else{
					if(mark==0)
						f->lchild = p->lchild;
					else
						f->rchild = p->lchild;
				}	
				free(p);
				p = NULL;
				taller = TRUE;	
			}
			else if(p->lchild==NULL && p->rchild!=NULL){//ֻ��������
				if(!f)//����� 
					T = p->rchild;			
				else{
					if(mark==0)
						f->lchild = p->rchild;
					else
						f->rchild = p->rchild;
				}	
				free(p);
				p = NULL;
				taller = TRUE;			
			}
			else if(p->lchild==NULL && p->rchild==NULL){//����������Ϊ��
				if(!f)//����� 
					T = NULL;			
				else{
					if(mark==0)
						f->lchild = NULL;
					else
						f->rchild = NULL;
				}	
				free(p);
				p = NULL;
				taller = TRUE;
			} 
			else{//��������������
				r = p->lchild;
				while(r->rchild)
					r = r->rchild;
				tmp = r->data;		
				taller = FALSE;
				if(!f)
					DeleteAVL(T, tmp, NULL, p, taller, mark);
				else{
					if(mark==0)
						DeleteAVL(f->lchild, tmp, NULL, p, taller, mark);
					else								
						DeleteAVL(f->rchild, tmp, NULL, p, taller, mark);	
				}
				p->data = tmp;
			} 
		}
		return OK;
	}
} 

int CreateAVL(BBSTree &T, int *N, int num){
	int i, t;
	T = NULL;
	if(N)
	{
		for(i=0; i<num; i++)
			InsertAVL(T, N[i], t);	
	}
	return OK;
}

int DepthAVL(BBSTree T){
	//��ƽ�������������� 
	int LD, RD; 
	if(T==NULL)
		return 0;							
	else
	{
		LD = DepthAVL(T->lchild);		
		RD = DepthAVL(T->rchild);		
		return (LD>=RD?LD:RD)+1;
	}
}

void PrintAVL(BBSTree T){
	//��ӡƽ������� 
	BBSTNode p[100][100] = {};
	int row, col;
	int i, j, k; 
	if(T){
		printf("ƽ�������������ʾ\n");
		row = DepthAVL(T);
		//col = pow(2, row) - 1;
		p[0][0] = *T;
		for(i = 1; i < row; i++){
			for(j = 0; j < pow(2, i); j++){
				if(j%2 == 0){
					if(p[i-1][j/2].lchild)
						p[i][j] = *(p[i-1][j/2].lchild);
				}
				else{
					if(p[i-1][j/2].rchild)
						p[i][j] = *(p[i-1][j/2].rchild);
				}
			}
		}
		k = pow(2, row);
		for(i=0; i<row; i++){
			for(j=0; j<pow(2, i); j++){
				if(p[i][j].data)
					printf("%*s%2d%*s", k-1, "", p[i][j].data, k-1, "");
				else
					printf("%*s%*s%*s", k-1, "", 2, "", k-1, "");
			}
			k = k/2;
			printf("\n");
		}
	}
	else
		printf("��ǰΪ����\n");
} 

void Split(BBSTree T, int e, BBSTree &T1, BBSTree &T2){
	int taller = 0;
	if(!T)
		return ;
	Split(T->lchild, e, T1, T2);
	if(e < T->data)
		InsertAVL(T2,T->data,taller);
	else
		InsertAVL(T1,T->data,taller);
	Split(T->rchild,e,T1,T2);
}

void SplitAVL(BBSTree T, int e, BBSTree &T2, BBSTree &T3){
	//�ݹ����Split�������ѳ����Ŷ����� 
	BBSTree t1 = NULL,t2 = NULL;
	Split(T, e, t1, t2);
	T2 = t1;
	T3 = t2;
	return ;
}

void MergeAVL(BBSTree &T1, BBSTree &T2){
	//�ݹ�ϲ����Ŷ����� 
	int taller = 0;
	if(!T2)
		return ;
	MergeAVL(T1, T2->lchild);
	InsertAVL(T1, T2->data, taller);
	MergeAVL(T1, T2->rchild);
}

int main(){
	BBSTree T1 = NULL, T2 = NULL, T3 = NULL;
	int t=0, taller;
	int i=0;
	int N[12] = {88, 29, 91, 19, 50, 32, 24, 45, 62, 79, 52, 67};
	int num = 12;
	printf("������ƽ�������T1:\n"); 
	CreateAVL(T1, N, num);//���� 
	PrintAVL(T1);
	while(1){
		printf("���������ţ�1���鿴T1 2������T1 3��ɾ��T1 4������T1��T2��T3 5���鿴T2 6���鿴T3 7���ϲ� 8���뿪:\n");
		scanf("%d", &t);
		switch(t){
			case 1:
				PrintAVL(T1);
				break;
			case 2:
				printf("����Ҫ���������: \n");
				scanf("%d",&t);
				InsertAVL(T1, t, taller); 
				PrintAVL(T1);
				break; 
			case 3:
				printf("����Ҫɾ��������: \n");
				scanf("%d", &t);
				DeleteAVL(T1, t, NULL, T1, taller, 0);
				PrintAVL(T1);
				break; 
			case 4:
				printf("��������ٽ�ֵ: \n");
				scanf("%d", &t);
				SplitAVL(T1, t, T2, T3);
				PrintAVL(T2);
				PrintAVL(T3);
				break; 
			case 5:
				PrintAVL(T2);
				break;
			case 6:
				PrintAVL(T3);
				break;
			case 7:
				printf("����1�ϲ�T1,T2, ����2�ϲ�T1,T3, ����3�ϲ�T2,T3: ");
				scanf("%d",&t);
				switch(t){
					case 1:
						MergeAVL(T1, T2);
						printf("�ϲ���T3����: \n"); 
						PrintAVL(T3);
						break;
					case 2:
						MergeAVL(T1, T3);
						printf("�ϲ���T2����: \n"); 
						PrintAVL(T2);
						break;
					case 3:
						MergeAVL(T2, T3);
						printf("�ϲ���T1����: \n"); 
						PrintAVL(T1);
						break;
					default:
						printf("�Ƿ�����!\n");
						break; 
				} 
				break; 
			case 8:
				exit(0);
			default: 
				printf("�Ƿ�����!\n"); 
				break;
		} 
	}
}
