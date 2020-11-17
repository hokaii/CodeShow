#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>//用于存储变长参数表 
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef char TElemType;
typedef struct CSTNode{
	TElemType data;//数据域 
	struct CSTNode *firstChild, *nextSibling;//最左孩子指针,右兄弟指针 
} CSTNode, *CSTree, *CSForest;//孩子兄弟链表
 
int InitTree(CSTree &T){
	//构造空树T
	T = (CSTree)malloc(sizeof(CSTNode));
	T->data = NULL;
	T->firstChild = T->nextSibling = NULL;
	return OK;
}

void AddTree(CSTree &T, TElemType e, int i){//i为0插入为孩子, 1插入为兄弟 
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
	//创建根节点e和n颗子树的树
	int i;
	CSTree t,p,pi;
	va_list argptr;//argptr是存放变长参数表信息的数组
	t = (CSTree)malloc(sizeof(CSTNode));
	if(!t)
		return NULL;
	t->data = e;//根节点的值为e 
	t->firstChild = t->nextSibling = NULL;
	if(n <= 0)//若无子树,返回根节点 
		return t;
	va_start(argptr, n);//令argptr指向参数n后的第一个实参 
	p = va_arg(argptr, CSTree);//取第一颗子树的实参并转换为CSTree类型 
	t->firstChild = p;
	pi = p;
	for(i=1; i<n; i++){//将n颗树作为根节点的子树插入 
		p = va_arg(argptr, CSTree);//取下一颗子树的实参并转换为CSTree类型 
		pi->nextSibling = p;
		pi = p;
	} 
	va_end(argptr);//取实参结束 
	return t;
}

int DestroyTree(CSTree &T){
	//销毁树T
	
}

int TreeDepth(CSTree T){
	//返回树T的深度
	
}

CSTNode *Search(CSTree T, TElemType e){
	//查找树T中的结点e并返回其指针
	
}

int InsertChild(CSTree &T, int i, CSTree c){
	//插入c为T的第i颗子树, c非空并与T不相交
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
	//删除T的第i颗子树
	
}

int PreOrderTraverseForest(CSForest F, int(*visit)(TElemType)){
	//先序遍历森林F
	if(NULL == F)
		return OK;
	if(ERROR == visit(F->data))
		return ERROR;
	if(ERROR == PreOrderTraverseForest(F->firstChild, visit));
		return ERROR;
	return PreOrderTraverseForest(F->nextSibling, visit); 
}

int ForestDepth(CSForest F){
	//求森林的深度 
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
	//查找森林F中的结点e并返回其指针
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
