#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define OK 1
#define LH +1 //左子树比右子树高,简称左高 
#define EH 0 //左、右子等高, 简称等高 
#define RH -1 //右子树比左子树高，简称右高

typedef struct BBSTNode{ 
	int data;
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

void LeftBalance(BBSTree &T){
	//实现对树T的左平衡处理
	BBSTree lc, rd;
	lc = T->lchild;
	switch(lc->bf){
		case LH://左高 
			T->bf = lc->bf = EH;
			R_Rotate(T);
			break;
		case RH://右高 
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

int InsertAVL(BBSTree &T, int e, int &taller){
	//实现对e插入到二叉树的操作
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
	//p指向当前结点，f指向p的父结点，初始化为空，*taller初始化为FALSE，mark代表f与p的关系，初始化为0 
	BBSTree r;
	int tmp;
	if(!p)
		return ERROR;
	else{		
		if(e < p->data){//搜寻左子树	
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
		else if(e > p->data){	//搜寻右子树
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
			if(p->lchild!=NULL && p->rchild==NULL){//只有左子树
				if(!f)//根结点 
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
			else if(p->lchild==NULL && p->rchild!=NULL){//只有右子树
				if(!f)//根结点 
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
			else if(p->lchild==NULL && p->rchild==NULL){//左右子树均为空
				if(!f)//根结点 
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
			else{//左右子树均不空
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
	//求平衡二叉树树的深度 
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
	//打印平衡二叉树 
	BBSTNode p[100][100] = {};
	int row, col;
	int i, j, k; 
	if(T){
		printf("平衡二叉树如下所示\n");
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
		printf("当前为空树\n");
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
	//递归调用Split函数分裂成两颗二叉树 
	BBSTree t1 = NULL,t2 = NULL;
	Split(T, e, t1, t2);
	T2 = t1;
	T3 = t2;
	return ;
}

void MergeAVL(BBSTree &T1, BBSTree &T2){
	//递归合并两颗二叉树 
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
	printf("测试用平衡二叉树T1:\n"); 
	CreateAVL(T1, N, num);//测试 
	PrintAVL(T1);
	while(1){
		printf("输入操作序号：1、查看T1 2、插入T1 3、删除T1 4、分裂T1到T2和T3 5、查看T2 6、查看T3 7、合并 8、离开:\n");
		scanf("%d", &t);
		switch(t){
			case 1:
				PrintAVL(T1);
				break;
			case 2:
				printf("输入要插入的数字: \n");
				scanf("%d",&t);
				InsertAVL(T1, t, taller); 
				PrintAVL(T1);
				break; 
			case 3:
				printf("输入要删除的数字: \n");
				scanf("%d", &t);
				DeleteAVL(T1, t, NULL, T1, taller, 0);
				PrintAVL(T1);
				break; 
			case 4:
				printf("输入分裂临界值: \n");
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
				printf("输入1合并T1,T2, 输入2合并T1,T3, 输入3合并T2,T3: ");
				scanf("%d",&t);
				switch(t){
					case 1:
						MergeAVL(T1, T2);
						printf("合并到T3如下: \n"); 
						PrintAVL(T3);
						break;
					case 2:
						MergeAVL(T1, T3);
						printf("合并到T2如下: \n"); 
						PrintAVL(T2);
						break;
					case 3:
						MergeAVL(T2, T3);
						printf("合并到T1如下: \n"); 
						PrintAVL(T1);
						break;
					default:
						printf("非法输入!\n");
						break; 
				} 
				break; 
			case 8:
				exit(0);
			default: 
				printf("非法输入!\n"); 
				break;
		} 
	}
}
