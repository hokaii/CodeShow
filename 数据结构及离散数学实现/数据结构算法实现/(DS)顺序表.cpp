#include <stdio.h>
#include <stdlib.h>
#define ERROR 0
#define OVERFLOW -1
#define OK 1

typedef struct{
	int *elem;
	int length;//当前长度 
	int size;//存储容量 
	int increment;//扩容的增量 
}SqList;//顺序表 

int InitList_Sq(SqList &L, int size, int inc){//初始化 
	L.elem = (int*)malloc(size*sizeof(int));
	if(L.elem == NULL)
		return OVERFLOW;
	L.length = 0;
	L.size = size;
	L.increment = inc;
	return OK;
}

bool ListEmpty_Sq(SqList L){//判断是否为空 
	if(L.length == 0){
		return true;
	}
	else
		return false;
}

int ListLength_Sq(SqList L){//返回元素个数 
	return L.length;
}

int GetElem_Sq(SqList L, int i, int &e){//用e返回表中第i个元素的值 
	if(i < 0 || i >= L.length){
		printf("传入元素位数错误!");
		return ERROR;
	}
	e = L.elem[i];
	return OK;
}

int Search_Sq(SqList L, int e){//顺序查找 
	for(int i = 0;i<L.length;i++){
		if(L.elem[i] == e)
			return i;
	}
	return -1;
}

int ListTraverse_Sq(SqList L, int(*visit)(int e)){//遍历 
	printf("visit: ");
	for(int i = 0; i < L.length ; i++){
		visit(L.elem[i]);
	}
	printf("\n");
	return OK;
}

int visit(int e){
	printf(" %d, ", e);
}

int putElem_Sq(SqList &L, int i, int e){//将表中第i个元素赋值为e 
	if(i < 0 || i >= L.length){
		printf("传入元素位数错误!");
		return ERROR;
	}
	L.elem[i] = e;
	return OK;
}

int Append_Sq(SqList &L, int e){//在表尾添加元素e 
	if(L.length == L.size){
		int *newbase = (int *)realloc(L.elem, (L.size+L.increment)*sizeof(int));
		if(NULL == newbase)
			return ERROR;
		L.elem = newbase;
		L.size += L.increment;
	}
	L.elem[L.length] = e;
	L.length++;
	return OK;
}

int DeleteLast_Sq(SqList &L, int &e){//删除表尾元素 
	if(L.length == 0){
		printf("顺序表为空");
		return ERROR; 
	}
	e = L.elem[L.length-1];
	L.length--;
	return OK;
}

void MergeList_Sq(SqList La, SqList Lb, SqList &Lc){
	int i=0, j=0;
	InitList_Sq(Lc, La.length+Lb.length, 5);
	while(i<La.length && j<Lb.length){
		if(La.elem[i] < Lb.elem[j]){
			Append_Sq(Lc, La.elem[i]);
			i++;
		}
		else{
			Append_Sq(Lc, Lb.elem[j]);
			j++;
		}
	}
	if(i < La.length){
		for(i; i<La.length; i++)
			Append_Sq(Lc, La.elem[i]);
	}
	if(j < Lb.length){
		for(j; j<Lb.length; j++)
			Append_Sq(Lc, Lb.elem[j]);
	}
}

void CreateList_Sq(SqList &L, int n, int *A){
	for(int i=0; i<n; i++){
		Append_Sq(L, A[i]);
	}
}

void CreateList_Sq_Sort(SqList &L, int n, int *A){//直接插入排序算法用 
	//Append_Sq(L, 0);
	for(int i=0; i<n; i++){
		Append_Sq(L, A[i]);
	}
}

void InsertSort(SqList &L){//直接排序算法 
	int i, j;
	for(i=1;i<L.length;i++)
		if(L.elem[i] > L.elem[i+1]){
			L.elem[0] = L.elem[i+1];
			j=i+1;
			do{
				j--;
				L.elem[j+1] = L.elem[j];
			}while(L.elem[0] < L.elem[j-1]);
			L.elem[j] = L.elem[0];
		}
	L.elem[0] = 0;
}

void ShellInsert(SqList &L, int dk){//一趟希尔排序 
	int i,j;
	for(i=1; i<L.length-dk;i++)
		if(L.elem[i] > L.elem[i+dk]){
			L.elem[0] = L.elem[i+dk];
			j=i+dk;
			do{
				j=j-dk;
				L.elem[j+dk] = L.elem[j];
			}while(j-dk>0 && L.elem[0] < L.elem[j-dk]);//注意这里必须多加j-dk>0的判断条件 
			L.elem[j] = L.elem[0];
		}
	L.elem[0] = 0;
}

void ShellSort(SqList &L, int d[], int n){//希尔排序 
	int k;
	for(k=0;k<n;k++)
		ShellInsert(L, d[k]);
}

//-------------------------------测试---------------------------------
bool Re(SqList &L){
	if(L.length==0||L.length==1)
		return true;
	int k;
	for(int i=0;i<L.length-1;i++){
		for(int j=0;j<L.length-1-i;j++){
			k=L.elem[j];
			L.elem[j]=L.elem[j+1];
			L.elem[j+1]=k;
		}
	}
	return true;
} 

bool Reverse(SqList &L){
	int temp;
	for(int i=0;i<L.length/2;i++){
		temp = L.elem[i];
		L.elem[i] = L.elem[L.length-1-i];
		L.elem[L.length-1-i]=temp;
	}
}

bool Del_Num(SqList &L, int s, int t){
	if(s>=t || L.length==0)
		return false;
	int i,j;
	int len=0, pos=0;
	for(i=0; i<L.length; i++){
		if(L.elem[i] >= s){
			pos=i; len=1;
			for(j=i+1;j<L.length;j++)
				if(L.elem[j]<=t)
					len++;
			break;
		}
	}
	for(i=pos+len; i<L.length; i++){
		printf("%d, %d\t",len,pos);
		L.elem[i-len] = L.elem[i];
	}
	L.length = L.length-len;
	return true;
}

bool del_s_t(SqList &L, int s, int t){
	int k=0,i;
	for(i=0;i<L.length;i++){
		if(L.elem[i]<s||L.elem[i]>t){
			L.elem[k]=L.elem[i];
			k++;
		}
	}
	L.length=k;
	return true;
}

void del_repeat(SqList &L){
	int i,j,k;
	for(i=0;i<L.length;i++){
		k=0;
		for(j=i+1;j<L.length;j++){
			if(L.elem[j]==L.elem[i])
				k++;
			else
				L.elem[j-k]=L.elem[j];
		}
		L.length-=k;
	}
}

int main(){
	SqList La;
	//直接排序算法测试 
	int A[8] = {25,45,56,68,90,38,10,72};
	int B[8] = {10,25,38,45,56,68,72,90};
	int C[8] = {10,10,48,90,48,70,10,90};
	InitList_Sq(La, 10, 5);
	CreateList_Sq_Sort(La, 8, C);
	ListTraverse_Sq(La, visit);
	
	del_repeat(La);
	printf("\n");
	ListTraverse_Sq(La, visit);
	
	//CreateList_Sq_Sort(La, 8, A);
	//ListTraverse_Sq(La, visit);
	//ShellSort(La, d, 3);
	//InsertSort(La);
	//ListTraverse_Sq(La, visit);
	//顺序表测试 
	/*InitList_Sq(La, 4, 5);
	SqList Lb;
	InitList_Sq(Lb, 4, 5);
	Append_Sq(La, 2);
	Append_Sq(La, 7);
	Append_Sq(La, 10);
	Append_Sq(La, 17);
	Append_Sq(Lb, 4);
	Append_Sq(Lb, 7);
	Append_Sq(Lb, 12);
	Append_Sq(Lb, 13);
	SqList Lv;
	MergeList_Sq(La,Lb,Lv);
	ListTraverse_Sq(Lv, visit);*/
}
