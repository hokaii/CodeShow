#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>//���ڴ洢�䳤������ 
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef char TElemType;
typedef struct CSTNode{
	TElemType data;//������ 
	struct CSTNode *firstChild, *nextSibling;//������ָ��,���ֵ�ָ�� 
} CSTNode, *CSTree, *CSForest;//�����ֵ�����
 
int InitTree(CSTree &T){
	//�������T
	T = (CSTree)malloc(sizeof(CSTNode));
	T->data = NULL;
	T->firstChild = T->nextSibling = NULL;
	return OK;
}

void AddTree(CSTree &T, TElemType e, int i){//iΪ0����Ϊ����, 1����Ϊ�ֵ� 
	if(T->data == NULL)
		T->data = e;
	else{
		CSTree p = (CSTree)malloc(sizeof(CSTNode));
		p->data = e;
		p->firstChild = NULL;
		p->nextSibling = NULL; 
		if(i)
			T->nextSibling = p;
		else
			T->firstChild = p;
	}
}

CSTree MakeTree(TElemType e, int n, ...){
	//�������ڵ�e��n����������
	int i;
	CSTree t,p,pi;
	va_list argptr;//argptr�Ǵ�ű䳤��������Ϣ������
	t = (CSTree)malloc(sizeof(CSTNode));
	if(!t)
		return NULL;
	t->data = e;//���ڵ��ֵΪe 
	t->firstChild = t->nextSibling = NULL;
	if(n <= 0)//��������,���ظ��ڵ� 
		return t;
	va_start(argptr, n);//��argptrָ�����n��ĵ�һ��ʵ�� 
	p = va_arg(argptr, CSTree);//ȡ��һ��������ʵ�β�ת��ΪCSTree���� 
	t->firstChild = p;
	pi = p;
	for(i=1; i<n; i++){//��n������Ϊ���ڵ���������� 
		p = va_arg(argptr, CSTree);//ȡ��һ��������ʵ�β�ת��ΪCSTree���� 
		pi->nextSibling = p;
		pi = p;
	} 
	va_end(argptr);//ȡʵ�ν��� 
	return t;
}

int DestroyTree(CSTree &T){
	//������T
	
}

int TreeDepth(CSTree T){
	//������T�����
	
}

CSTNode *Search(CSTree T, TElemType e){
	//������T�еĽ��e��������ָ��
	
}

int InsertChild(CSTree &T, int i, CSTree c){
	//����cΪT�ĵ�i������, c�ǿղ���T���ཻ
	int j;
	CSTree p;
	if(T == NULL || i<1)
		return ERROR;
	if(i == 1){
		c->nextSibling = T->firstChild;
		T->firstChild = c;
	}
	else{
		p = T->firstChild;
		for(j=2; j<i && p!=NULL; j++)
			p = p->nextSibling;
		if(j == i){
			c->nextSibling = p->nextSibling;
			p->nextSibling = c;
		}
		else
			return ERROR;	
	}
	return OK;
}


int DeleteChild(CSTree &T, int i){
	//ɾ��T�ĵ�i������
	
}

int PreOrderTraverseForest(CSForest F, int(*visit)(TElemType)){
	//�������ɭ��F
	if(NULL == F)
		return OK;
	if(ERROR == visit(F->data))
		return ERROR;
	if(ERROR == PreOrderTraverseForest(F->firstChild, visit));
		return ERROR;
	return PreOrderTraverseForest(F->nextSibling, visit); 
}

int ForestDepth(CSForest F){
	//��ɭ�ֵ���� 
	int dep1, dep2, dep;
	if(NULL == p)
		dep = 0;
	else{
		dep1 = ForestDepth(F->firstChild)+1;
		dep2 = ForestDepth(F->nextSibling);
		dep = dep1>dep2?dep1:dep2;
	}
	return dep;
}

CSTNode *Search(CSForest F, TElemType e){
	//����ɭ��F�еĽ��e��������ָ��
	CSTNode *result = NULL;
	if(NULL == F)
		return NULL;
	if(F->data == e)
		return F;
	if((result = Search(F->firstChild, e)) != NULL) 
		return result;
	return Search(F->nextSibling, e);
}

int main(){
	CSTree t;
	InitTree(t);
	AddTree(t, 'A', 1);
}
